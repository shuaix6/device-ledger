import json

devices = [
    {"name":"数控机床","model":"CNC-850","power":15.5,"location":"3号车间"},
]

f = open("devices_out.json","w",encoding="utf-8")
json.dump(devices, f,ensure_ascii=False,indent=4)
f.close()