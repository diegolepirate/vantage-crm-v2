"""
Build fake-data.js with the 783 REAL Crete prospects scraped from OSM,
plus synthetic clients/projects/calls layered on top so the CRM has the
stats it needs to render correctly.
"""
import csv
import json

import random
random.seed(42)

import os, re

def load(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

osm    = load("prospects_crete.csv")
vrisko = load("prospects_vrisko.csv")
print(f"OSM:    {len(osm)}")
print(f"Vrisko: {len(vrisko)}")

# Merge with phone-based dedup (same business in both sources -> keep one)
seen = set()
rows = []
for src in (vrisko, osm):       # Vrisko first: paid listings have richer addr
    for r in src:
        # Use full normalized phone (12 digits = "30" + 10) as dedup key.
        # Anything shorter collapses different businesses sharing area prefix.
        key = re.sub(r"\D", "", r.get("numero",""))
        if not key or key in seen:
            continue
        seen.add(key)
        # Strip source label so CRM treats every prospect identically
        notes = (r.get("notes") or "").strip()
        notes = re.sub(r"^(Vrisko|OSM)\s+\S+\s*", "", notes).strip()
        r["notes"] = notes
        rows.append(r)

print(f"After dedup: {len(rows)} unique prospects")
# Cap at 15k for page-load speed while keeping full geographic coverage
CAP = 12000
if len(rows) > CAP:
    # Stratified sample: keep proportional family distribution
    by_fam = {}
    for r in rows:
        by_fam.setdefault(r["famille"], []).append(r)
    sampled = []
    for fam, group in by_fam.items():
        n = max(1, int(round(len(group) * CAP / len(rows))))
        random.shuffle(group)
        sampled.extend(group[:n])
    random.shuffle(sampled)
    rows = sampled[:CAP]
    print(f"Sampled down to {len(rows)} (stratified by famille)")

# Map -> JS-friendly objects
real_prospects = []
for i, r in enumerate(rows, start=1):
    real_prospects.append({
        "id": i,
        "nom": r["nom"],
        "numero": r["numero"],
        "type_tel": r["type_tel"],
        "famille": r["famille"],
        "categorie": r["categorie"] or "",
        "region": "Crete",
        "vendeur": "",
        "status": "nouveau",
        "notes": r.get("notes", ""),
        "email": "",
        "instagram": "",
        "facebook": "",
        "rating": 0,
        "adresse": r.get("adresse", ""),
        "blacklisted": False,
    })

prospects_json = json.dumps(real_prospects, ensure_ascii=False)

js = """// fake-data.js — REAL Crete prospects (OSM Overpass scrape) + synthetic
// clients/projects/calls layered on top for CRM stats.
(function(){
  var REAL_PROSPECTS = """ + prospects_json + """;

  var ST=['nouveau','appele','negociation','gagne','rappeler','maintenance','perdu'];
  var SW=[60,15,8,7,5,3,2];      // overwhelmingly "nouveau" since these are fresh leads
  var VD=['vendeur 1','vendeur 2','vendeur 3'];
  var NT=['','','','','','Bon contact','RDV pris','Demande devis','A rappeler','Tres motive'];
  var FNA=['Nikos','Maria','Dimitris','Elena','Kostas','Sofia','Yannis','Anna','Giorgos','Katerina'];
  var LNA=['Papadopoulos','Nikolaou','Georgiou','Vasileiou','Konstantinou','Karagiannis','Pappas'];

  function pk(a){return a[Math.floor(Math.random()*a.length)]}
  function ri(a,b){return Math.floor(Math.random()*(b-a+1))+a}
  function wp(it,w){var t=0,i;for(i=0;i<w.length;i++)t+=w[i];var r=Math.random()*t,c=0;for(i=0;i<it.length;i++){c+=w[i];if(r<=c)return it[i]}return it[it.length-1]}
  function rd(d){var x=new Date();x.setDate(x.getDate()-ri(0,d));x.setHours(ri(8,20),ri(0,59),ri(0,59));return x.toISOString()}

  // Hydrate real prospects with realistic timeline + status mix
  var P = REAL_PROSPECTS.map(function(p){
    var st = wp(ST, SW);
    var v  = st === 'nouveau' ? (Math.random() > 0.7 ? pk(VD) : '') : pk(VD);
    var cr = rd(120);
    return Object.assign({}, p, {
      status: st,
      vendeur: v,
      notes: p.notes || pk(NT),
      created_at: cr,
      updated_at: cr,
      last_called_at: st !== 'nouveau' ? rd(30) : null,
      total_calls: st === 'nouveau' ? 0 : ri(1, 12),
      call_duration_total: st === 'nouveau' ? 0 : ri(30, 900),
      call_date: st !== 'nouveau' ? rd(14) : null
    });
  });

  // Clients = prospects in advanced statuses
  var CST=['gagne','negociation','maintenance','rappeler'];
  var C=[], cid=1;
  P.forEach(function(p){
    if (CST.indexOf(p.status) >= 0) {
      C.push({
        id: cid++, prospect_id: p.id, nom: p.nom, numero: p.numero,
        email: p.email, instagram: p.instagram, facebook: '',
        region: p.region, famille: p.famille,
        vendor_name: p.vendeur, business_name: p.nom,
        contact_name: pk(FNA) + ' ' + pk(LNA),
        sale_price: [350, 450, 500, 600, 750, 900][ri(0,5)],
        site_status: p.status, project_id: null, hidden_by: [],
        notes: p.notes, with_maintenance: Math.random() > 0.7, delivery_notes: '',
        created_at: p.created_at, updated_at: p.updated_at
      });
    }
  });

  // One Crete project
  var PJ = [
    { id:1, name:'Conquete Crete', region:'Crete',
      vendor:'vendeur 1', vendeur:'vendeur 1', type:'all', families:'[]',
      target_sales:50, target_calls:500, status:'active',
      created_at: rd(60), updated_at: rd(5) }
  ];
  C.slice(0, Math.min(20, C.length)).forEach(function(c){ c.project_id = 1 });

  // Synthetic call history
  var CH = [];
  for (var j = 0; j < 500; j++) {
    var pr = pk(P);
    CH.push({
      id: j+1, prospect_id: pr.id, prospect_name: pr.nom,
      vendor_name: pk(VD), duration: ri(15, 300),
      outcome: pk(['answered','no_answer','voicemail','busy','callback']),
      notes: pk(NT), created_at: rd(30)
    });
  }

  var VS = VD.map(function(v, i){
    return {
      id: i+1, vendor_name: v,
      total_calls: ri(150, 600), total_duration: ri(15000, 60000),
      total_won: ri(8, 35), total_lost: ri(3, 15),
      current_streak: ri(1, 12), longest_streak: ri(8, 25),
      last_call_date: new Date().toISOString().slice(0,10),
      total_points: ri(400, 1500),
      created_at: rd(90), updated_at: rd(1)
    };
  });

  window.FAKE_PROSPECTS         = P;
  window.FAKE_CLIENTS           = C;
  window.FAKE_PROJECTS          = PJ;
  window.FAKE_CALLS             = CH;
  window.FAKE_VENDOR_STATS      = VS;
  window.FAKE_REMINDERS         = [];
  window.FAKE_BLACKLIST         = [];
  window.FAKE_SCRIPTS           = [];
  window.FAKE_BADGES            = [];
  window.FAKE_PROSPECT_HISTORY  = [];
  window.FAKE_PROJECT_OBJECTIVES= [];
  window.FAKE_ACTIVITY_LOG      = [];
  window.FAKE_VENDOR_BADGES     = [];
  console.log('CRM: ' + P.length + ' real Crete prospects, ' + C.length + ' clients, ' + PJ.length + ' projets');
})();
"""

with open("fake-data.js", "w", encoding="utf-8") as f:
    f.write(js)

print(f"Wrote fake-data.js with {len(real_prospects)} real prospects")
