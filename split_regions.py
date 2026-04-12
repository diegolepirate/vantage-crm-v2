import json, os
from supabase import create_client

# Get Supabase creds from index.html
with open('vantage-crm/index.html','r',encoding='utf-8') as f:
    html = f.read()

import re
url_match = re.search(r"createClient\(['\"]([^'\"]+)['\"]", html)
key_match = re.search(r"createClient\([^,]+,\s*['\"]([^'\"]+)['\"]", html)
if not url_match or not key_match:
    print("Can't find Supabase creds")
    exit(1)

SUPA_URL = url_match.group(1)
SUPA_KEY = key_match.group(1)
print(f"URL: {SUPA_URL[:30]}...")

sb = create_client(SUPA_URL, SUPA_KEY)

# Fetch all Attique prospects
print("Fetching Attique prospects...")
attique_ids = []
start = 0
while True:
    r = sb.table('prospects').select('id').eq('region','Attique — Athènes et banlieue').range(start, start+999).execute()
    if not r.data: break
    attique_ids.extend([d['id'] for d in r.data])
    start += 1000
print(f"Found {len(attique_ids)} Attique prospects")

# Split in 2
mid = len(attique_ids) // 2
part1 = attique_ids[:mid]
part2 = attique_ids[mid:]
print(f"Part 1: {len(part1)}, Part 2: {len(part2)}")

# Update part 1
print("Updating Attique Partie 1...")
for i in range(0, len(part1), 500):
    batch = part1[i:i+500]
    sb.table('prospects').update({'region': 'Attique — Athènes Partie 1'}).in_('id', batch).execute()
    print(f"  batch {i//500+1} done")

print("Updating Attique Partie 2...")
for i in range(0, len(part2), 500):
    batch = part2[i:i+500]
    sb.table('prospects').update({'region': 'Attique — Athènes Partie 2'}).in_('id', batch).execute()
    print(f"  batch {i//500+1} done")

# Fetch all Autres prospects
print("\nFetching Autres prospects...")
autres_ids = []
start = 0
while True:
    r = sb.table('prospects').select('id').eq('region','Autres').range(start, start+999).execute()
    if not r.data: break
    autres_ids.extend([d['id'] for d in r.data])
    start += 1000
print(f"Found {len(autres_ids)} Autres prospects")

# Split in 3
third = len(autres_ids) // 3
mix1 = autres_ids[:third]
mix2 = autres_ids[third:third*2]
mix3 = autres_ids[third*2:]
print(f"Mix 1: {len(mix1)}, Mix 2: {len(mix2)}, Mix 3: {len(mix3)}")

print("Updating Mix 1...")
for i in range(0, len(mix1), 500):
    batch = mix1[i:i+500]
    sb.table('prospects').update({'region': 'Mix 1'}).in_('id', batch).execute()
    print(f"  batch {i//500+1} done")

print("Updating Mix 2...")
for i in range(0, len(mix2), 500):
    batch = mix2[i:i+500]
    sb.table('prospects').update({'region': 'Mix 2'}).in_('id', batch).execute()
    print(f"  batch {i//500+1} done")

print("Updating Mix 3...")
for i in range(0, len(mix3), 500):
    batch = mix3[i:i+500]
    sb.table('prospects').update({'region': 'Mix 3'}).in_('id', batch).execute()
    print(f"  batch {i//500+1} done")

print("\nDONE!")
