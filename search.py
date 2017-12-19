import json, re, sys

matches = {}
patterns = []
for arg in sys.argv: 
  patterns.append(re.compile(arg))

with open("results.txt", "r") as f:
  data = json.loads(f.read())

for region in data.keys():
  for ami in data[region].keys():
    raw = json.dumps(data[region][ami])
    matched = False
    for p in patterns:
      if p.search(raw):
        matched = True
    if matched:
      if region not in matches.keys():
        matches[region] = {}
      if ami not in matches[region].keys():
        matches[region][ami] = data[region][ami]

print json.dumps(matches,indent=2)
