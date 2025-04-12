import json
import sys

data = []
lines = map(lambda x: x.strip()[4:-4].split(), sys.stdin.readlines())
for line in lines:
    im = float(line[-1])
    if line[1] == "-":
        im = -im
    data.append({"Re": float(line[0]), "Im": im})
with open('output.json', 'w+') as file:
    file.write(json.dumps({"complex": data}))