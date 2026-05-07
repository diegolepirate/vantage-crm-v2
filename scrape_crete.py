"""
Scrape Crete businesses WITHOUT a website but WITH a phone, from OpenStreetMap
Overpass API. Output a CSV ready to import into the Vantage CRM `prospects`
table (matches the existing schema: nom, numero, type_tel, famille, categorie,
region, adresse, rating, avis, ...).

Usage:  python scrape_crete.py
Output: prospects_crete.csv  +  prospects_crete.sql
"""

import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request

OVERPASS = "https://overpass-api.de/api/interpreter"

# Greece bounding box (south, west, north, east) — full country incl. islands
BBOX = (34.70, 19.30, 41.80, 29.70)

# OSM tag -> CRM "famille" mapping
FAMILY_MAP = {
    # restaurant + food
    "restaurant": "Restauration", "fast_food": "Restauration",
    "ice_cream": "Restauration", "food_court": "Restauration",
    # cafe & bar
    "cafe": "Cafe & Bar", "bar": "Cafe & Bar", "pub": "Cafe & Bar",
    "biergarten": "Cafe & Bar", "nightclub": "Cafe & Bar",
    # bakery
    "bakery": "Boulangerie", "pastry": "Boulangerie",
    "confectionery": "Boulangerie",
    # beauty
    "hairdresser": "Beauté", "beauty": "Beauté", "cosmetics": "Beauté",
    "perfumery": "Beauté", "tattoo": "Beauté", "massage": "Beauté",
    "nails": "Beauté",
    # health
    "pharmacy": "Santé", "dentist": "Santé", "doctors": "Santé",
    "doctor": "Santé", "veterinary": "Santé", "physiotherapist": "Santé",
    "optician": "Santé", "optometrist": "Santé", "psychotherapist": "Santé",
    "alternative": "Santé", "clinic": "Santé",
    # auto
    "car": "Auto", "car_repair": "Auto", "car_parts": "Auto",
    "motorcycle": "Auto", "motorcycle_repair": "Auto",
    "tyres": "Auto", "car_rental": "Auto", "car_wash": "Auto",
    "fuel": "Auto", "driving_school": "Auto", "mechanic": "Auto",
    "bicycle": "Auto",
    # crafts (artisans)
    "carpenter": "Artisans", "electrician": "Artisans",
    "plumber": "Artisans", "painter": "Artisans", "tiler": "Artisans",
    "blacksmith": "Artisans", "sawmill": "Artisans",
    "upholsterer": "Artisans", "locksmith": "Artisans",
    "hvac": "Artisans", "glaziery": "Artisans",
    "metal_construction": "Artisans", "sailmaker": "Artisans",
    "sculptor": "Artisans", "stonemason": "Artisans",
    "shoemaker": "Artisans", "tailor": "Artisans", "watchmaker": "Artisans",
    "winery": "Artisans", "brewery": "Artisans", "jeweller": "Artisans",
    "photographer": "Artisans",
    # services (offices etc.)
    "accountant": "Services", "lawyer": "Services",
    "insurance": "Services", "real_estate": "Services",
    "travel_agent": "Services", "employment_agency": "Services",
    "financial": "Services", "tax_advisor": "Services",
    "architect": "Services", "telecommunication": "Services",
    "laundry": "Services", "dry_cleaning": "Services",
    "copyshop": "Services", "photo": "Services",
    # tourism -> services
    "hotel": "Services", "guest_house": "Services", "hostel": "Services",
    "motel": "Services", "apartment": "Services", "chalet": "Services",
    # leisure -> services
    "fitness_centre": "Services", "sports_centre": "Services",
}

# everything else under shop/* not mapped above falls back to "Commerce".
DEFAULT_FAMILY = "Commerce"

QUERY = """
[out:json][timeout:600];
// Restrict to Greece's actual administrative boundary — no neighbour spillover
area["ISO3166-1"="GR"][admin_level=2]->.gr;
(
  nwr["amenity"~"^(restaurant|cafe|bar|pub|fast_food|ice_cream|bakery|pharmacy|dentist|doctors|veterinary|car_rental|car_wash|fuel|driving_school|clinic|nightclub|biergarten)$"](area.gr);
  nwr["shop"](area.gr);
  nwr["craft"](area.gr);
  nwr["tourism"~"^(hotel|guest_house|hostel|motel|apartment|chalet)$"](area.gr);
  nwr["office"](area.gr);
  nwr["healthcare"](area.gr);
  nwr["leisure"~"^(fitness_centre|sports_centre)$"](area.gr);
);
out tags center;
""".strip()


def fetch():
    print("[1/3] Querying Overpass (this can take 30-90s)...", flush=True)
    data = urllib.parse.urlencode({"data": QUERY}).encode()
    req = urllib.request.Request(OVERPASS, data=data, headers={
        "User-Agent": "vantage-crm-prospect-builder/1.0",
    })
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=400) as r:
        raw = r.read()
    print(f"    received {len(raw)/1024:.1f} KB in {time.time()-t0:.1f}s", flush=True)
    return json.loads(raw)


def has_website(t):
    for k in ("website", "contact:website", "url", "contact:url"):
        if t.get(k):
            return True
    return False


def get_phone(t):
    for k in ("contact:phone", "phone", "contact:mobile", "mobile"):
        if t.get(k):
            return t[k]
    return None


def normalize_phone(p):
    """Return canonical +30NNNNNNNNNN if Greek, '' otherwise."""
    if not p:
        return ""
    # Take first phone if multiple
    p = re.split(r"[;,/]| or | & ", p)[0].strip()
    digits = re.sub(r"[^\d+]", "", p)
    if not digits:
        return ""
    # Normalise leading 00 -> +
    if digits.startswith("00"):
        digits = "+" + digits[2:]
    # Reject any explicitly non-Greek country code
    if digits.startswith("+") and not digits.startswith("+30"):
        return ""
    # Strip "+30" or leading "30" if present
    if digits.startswith("+30"):
        local = digits[3:]
    elif digits.startswith("30") and len(digits) >= 12:
        local = digits[2:]
    else:
        local = digits.lstrip("+")
    # Greek phones are 10 digits starting with 2 (fixed) or 6 (mobile)
    if len(local) != 10 or local[0] not in ("2", "6"):
        return ""
    return "+30" + local


def phone_type(p):
    # GR mobile prefixes start with +306 (e.g. 6912345678)
    if p.startswith("+306") or p.startswith("306") or (p.startswith("6") and len(p) == 10):
        return "mobile"
    return "fixe"


def family_for(t):
    for tag in ("amenity", "shop", "craft", "tourism", "office", "healthcare", "leisure"):
        v = t.get(tag)
        if v and v in FAMILY_MAP:
            return FAMILY_MAP[v], v
    # shop fallback
    if t.get("shop"):
        return DEFAULT_FAMILY, t["shop"]
    if t.get("office"):
        return "Services", t["office"]
    if t.get("healthcare"):
        return "Santé", t["healthcare"]
    return DEFAULT_FAMILY, t.get("amenity") or t.get("shop") or "other"


def region_for(t):
    """Best-effort region label from address tags + lat/lon clues."""
    city = (t.get("addr:city") or t.get("addr:town") or t.get("addr:village")
            or t.get("addr:suburb") or "").strip()
    prov = (t.get("addr:province") or t.get("addr:state") or "").strip()
    if prov:
        return prov
    if city:
        return city
    return "Grece"


def build_address(t):
    parts = []
    street = t.get("addr:street") or ""
    house = t.get("addr:housenumber") or ""
    if street:
        parts.append((street + " " + house).strip())
    city = t.get("addr:city") or t.get("addr:town") or t.get("addr:village") or ""
    if city:
        parts.append(city)
    region = t.get("addr:province") or t.get("addr:state") or ""
    if region:
        parts.append(region)
    pc = t.get("addr:postcode") or ""
    if pc:
        parts.append(pc)
    return ", ".join([p for p in parts if p])


def main():
    js = fetch()
    elems = js.get("elements", [])
    print(f"[2/3] {len(elems)} raw OSM elements — filtering no-website + has-phone...", flush=True)

    seen = set()
    rows = []
    for e in elems:
        t = e.get("tags") or {}
        name = t.get("name") or t.get("name:en") or t.get("name:el")
        if not name:
            continue
        if has_website(t):
            continue
        phone = get_phone(t)
        if not phone:
            continue
        norm = normalize_phone(phone)
        if not norm:                       # non-Greek or invalid -> drop
            continue
        # dedup by name + first 8 digits of phone
        key = (name.strip().lower(), re.sub(r"\D", "", norm)[:8])
        if key in seen:
            continue
        seen.add(key)

        fam, sub = family_for(t)
        rows.append({
            "nom": name.strip(),
            "numero": norm,
            "type_tel": phone_type(norm),
            "famille": fam,
            "categorie": "",            # tier (A/B/C) left blank — to be enriched manually
            "region": region_for(t),
            "adresse": build_address(t),
            "rating": "",
            "avis": "",
            "vendeur": "",
            "status": "nouveau",
            "notes": f"OSM {sub}",
            "blacklisted": False,
        })

    print(f"[3/3] {len(rows)} prospects with valid phone & no website", flush=True)

    # CSV
    csv_path = "prospects_crete.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [
            "nom", "numero", "type_tel", "famille", "categorie", "region",
            "adresse", "rating", "avis", "vendeur", "status", "notes", "blacklisted",
        ])
        w.writeheader()
        w.writerows(rows)

    # SQL
    sql_path = "prospects_crete.sql"

    def esc(v):
        if v is None or v == "":
            return "NULL"
        if isinstance(v, bool):
            return "true" if v else "false"
        return "'" + str(v).replace("'", "''") + "'"

    with open(sql_path, "w", encoding="utf-8") as f:
        f.write("-- Crete prospects: businesses without website, with phone\n")
        f.write("-- Source: OpenStreetMap (Overpass API)\n")
        f.write(f"-- Count: {len(rows)}\n\n")
        for r in rows:
            f.write(
                "INSERT INTO prospects (nom, numero, type_tel, famille, categorie, "
                "region, adresse, rating, avis, vendeur, status, notes, blacklisted) "
                "VALUES ("
                + ", ".join([
                    esc(r["nom"]), esc(r["numero"]), esc(r["type_tel"]),
                    esc(r["famille"]), esc(r["categorie"]), esc(r["region"]),
                    esc(r["adresse"]), esc(r["rating"]), esc(r["avis"]),
                    esc(r["vendeur"]), esc(r["status"]), esc(r["notes"]),
                    esc(r["blacklisted"]),
                ]) + ");\n"
            )

    # Family breakdown
    breakdown = {}
    for r in rows:
        breakdown[r["famille"]] = breakdown.get(r["famille"], 0) + 1
    print("\nBreakdown by famille:")
    for k, v in sorted(breakdown.items(), key=lambda x: -x[1]):
        print(f"  {k:14s} {v}")
    print(f"\n[OK] {csv_path}  +  {sql_path}")


if __name__ == "__main__":
    main()
