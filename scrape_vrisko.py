"""
Vrisko.gr scraper — Greek Yellow Pages.
Extracts paid listings (highly reliable contacts) for Greek SMBs across all
major categories and cities. Filters to businesses WITHOUT a website.

Output: prospects_vrisko.csv (same schema as prospects_crete.csv).

Run:  python scrape_vrisko.py
"""

import csv
import re
import sys
import time

from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth


# (greek_query, famille, sub-type)
CATEGORIES = [
    ("εστιατόριο",         "Restauration", "restaurant"),
    ("ταβέρνα",            "Restauration", "taverna"),
    ("ψητοπωλείο",         "Restauration", "psitopoleio"),
    ("σουβλατζίδικο",      "Restauration", "souvlaki"),
    ("πιτσαρία",           "Restauration", "pizzeria"),
    ("καφετέρια",          "Cafe & Bar",   "cafe"),
    ("μπαρ",               "Cafe & Bar",   "bar"),
    ("καφενείο",           "Cafe & Bar",   "kafeneio"),
    ("αρτοποιείο",         "Boulangerie",  "bakery"),
    ("ζαχαροπλαστείο",     "Boulangerie",  "patisserie"),
    ("κρεοπωλείο",         "Commerce",     "butcher"),
    ("παντοπωλείο",        "Commerce",     "grocery"),
    ("κομμωτήριο",         "Beauté",       "hairdresser"),
    ("ινστιτούτο ομορφιάς", "Beauté",      "beauty"),
    ("μανικιούρ",          "Beauté",       "nails"),
    ("φαρμακείο",          "Santé",        "pharmacy"),
    ("οδοντίατρος",        "Santé",        "dentist"),
    ("ιατρός",             "Santé",        "doctor"),
    ("φυσιοθεραπευτής",    "Santé",        "physio"),
    ("κτηνίατρος",         "Santé",        "vet"),
    ("συνεργείο αυτοκινήτων","Auto",       "garage"),
    ("φανοποιείο",         "Auto",         "bodyshop"),
    ("βουλκανιζατέρ",      "Auto",         "tyres"),
    ("ηλεκτρολόγος",       "Artisans",     "electrician"),
    ("υδραυλικός",         "Artisans",     "plumber"),
    ("ξυλουργός",          "Artisans",     "carpenter"),
    ("ελαιοχρωματιστής",   "Artisans",     "painter"),
    ("σιδεράς",            "Artisans",     "blacksmith"),
    ("ξενοδοχείο",         "Services",     "hotel"),
    ("ενοικιαζόμενα δωμάτια","Services",   "guest_house"),
    ("λογιστής",           "Services",     "accountant"),
    ("δικηγόρος",          "Services",     "lawyer"),
    ("μεσιτικό γραφείο",   "Services",     "real_estate"),
    ("καθαριστήριο",       "Services",     "laundry"),
    ("κατάστημα ρούχων",   "Commerce",     "clothes"),
    ("υποδήματα",          "Commerce",     "shoes"),
    ("κοσμήματα",          "Commerce",     "jewelry"),
    ("ανθοπωλείο",         "Commerce",     "florist"),
    ("οπτικά",             "Santé",        "optician"),
    ("γυμναστήριο",        "Services",     "gym"),
]

CITIES = [
    "Αθήνα", "Θεσσαλονίκη", "Πάτρα", "Ηράκλειο", "Χανιά", "Ρόδος",
    "Λάρισα", "Βόλος", "Ιωάννινα", "Καλαμάτα",
]

MAX_PAGES = 5                  # per (category, city) combo
WAIT_PAGE = 2.5                # seconds between pages — be polite
WAIT_LISTING = 3.5             # seconds after first goto for Akamai pass

EXTRACT_JS = r"""
() => {
  const out = [];
  const items = document.querySelectorAll('.FreeListingItemBox, .PaidListingItemBox, [class*="ListingItemBox"]');
  items.forEach(el => {
    const name  = el.querySelector('[itemprop="name"]')?.innerText?.trim()    || '';
    const phone = el.querySelector('[itemprop="telephone"]')?.innerText?.trim()
              || el.querySelector('a[href^="tel:"]')?.getAttribute('href')?.replace('tel:','')?.trim()
              || '';
    const addr  = el.querySelector('[itemprop="address"]')?.innerText?.trim() || '';
    // Check explicit website link
    const website = el.querySelector('a[href^="http"][target="_blank"]:not([href*="vrisko.gr"]):not([href*="facebook"]):not([href*="instagram"])')?.href
                 || el.querySelector('[itemprop="url"]')?.getAttribute('content')
                 || '';
    const lat = el.querySelector('[itemprop="latitude"]')?.getAttribute('content') || '';
    const lon = el.querySelector('[itemprop="longitude"]')?.getAttribute('content') || '';
    const cat = (el.getAttribute('itemtype') || '').split('/').pop() || '';
    if (name) out.push({name, phone, addr, website, lat, lon, cat});
  });
  return out;
}
"""


def normalize_phone(p):
    if not p:
        return ""
    p = re.split(r"[;,/]", p)[0].strip()
    digits = re.sub(r"[^\d+]", "", p)
    if digits.startswith("00"):
        digits = "+" + digits[2:]
    if digits.startswith("+") and not digits.startswith("+30"):
        return ""
    if digits.startswith("+30"):
        local = digits[3:]
    elif digits.startswith("30") and len(digits) >= 12:
        local = digits[2:]
    else:
        local = digits.lstrip("+")
    if len(local) != 10 or local[0] not in ("2", "6"):
        return ""
    return "+30" + local


def save_csv(rows, path):
    if not rows:
        return
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main():
    rows = []
    seen = set()  # dedup by (name, phone-prefix)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context(locale="el-GR", viewport={"width": 1366, "height": 900})
        Stealth().apply_stealth_sync(ctx)
        page = ctx.new_page()

        # Warm-up: visit home so Akamai cookies set
        print("Warming up Vrisko session...", flush=True)
        page.goto("https://www.vrisko.gr/", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(3000)

        total_combos = len(CATEGORIES) * len(CITIES)
        done_combos = 0
        for query, famille, subtype in CATEGORIES:
            for city in CITIES:
                done_combos += 1
                page_num = 1
                empty_streak = 0
                while page_num <= MAX_PAGES:
                    url = f"https://www.vrisko.gr/search/{query}/{city}/?page={page_num}"
                    try:
                        page.goto(url, wait_until="domcontentloaded", timeout=30000)
                        page.wait_for_timeout(int(WAIT_LISTING * 1000) if page_num == 1 else int(WAIT_PAGE * 1000))
                    except Exception as e:
                        print(f"  ! goto failed: {e}", flush=True)
                        break
                    if "Access Denied" in page.title():
                        print("  ! Access Denied — pausing 30s", flush=True)
                        time.sleep(30)
                        continue
                    try:
                        listings = page.evaluate(EXTRACT_JS)
                    except Exception as e:
                        print(f"  ! evaluate failed: {e}", flush=True)
                        time.sleep(5)
                        break
                    if not listings:
                        empty_streak += 1
                        if empty_streak >= 2:
                            break
                    else:
                        empty_streak = 0

                    new_in_page = 0
                    for L in listings:
                        norm = normalize_phone(L["phone"])
                        if not norm:
                            continue
                        if L["website"]:                  # skip — has website
                            continue
                        key = (L["name"][:40].lower().strip(), norm[-8:])
                        if key in seen:
                            continue
                        seen.add(key)
                        rows.append({
                            "nom":        L["name"][:120],
                            "numero":     norm,
                            "type_tel":   "mobile" if norm.startswith("+306") else "fixe",
                            "famille":    famille,
                            "categorie":  "",
                            "region":     city,
                            "adresse":    L["addr"][:200],
                            "rating":     "",
                            "avis":       "",
                            "vendeur":    "",
                            "status":     "nouveau",
                            "notes":      f"Vrisko {subtype}",
                            "blacklisted": False,
                        })
                        new_in_page += 1
                    sys.stdout.write(
                        f"[{done_combos}/{total_combos}] {query[:14]:14s} / {city[:12]:12s} "
                        f"p{page_num} +{new_in_page} (total={len(rows)})\n"
                    )
                    sys.stdout.flush()
                    # Save progress every 200 rows in case of crash
                    if len(rows) and len(rows) % 200 == 0:
                        save_csv(rows, "prospects_vrisko.csv")
                    if len(listings) < 5:                # last page reached
                        break
                    page_num += 1

        browser.close()

    out = "prospects_vrisko.csv"
    save_csv(rows, out)

    breakdown = {}
    for r in rows:
        breakdown[r["famille"]] = breakdown.get(r["famille"], 0) + 1
    print("\n=== DONE ===")
    print(f"Total prospects: {len(rows)}")
    for k, v in sorted(breakdown.items(), key=lambda x: -x[1]):
        print(f"  {k:14s} {v}")
    print(f"\n[OK] {out}")


if __name__ == "__main__":
    main()
