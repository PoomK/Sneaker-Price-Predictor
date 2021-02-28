import json

with open("YzyBredData.json","r") as f:
    k = json.load(f)

p = k["series"][0]["data"]

print(p)