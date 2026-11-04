import json

with open("devices.json","r",encoding="utf-8") as fin:
    devices = json.load(fin)

for device in devices:
    print(f"{device['id']} {device['name']} {device['model']} {device['power']} {device['location']}")

print(f"共 {len(devices)} 台")
