import json
with open("devices.json","r",encoding="utf-8") as fin:
    devices = json.load(fin)
def show_all(data,limit=0):
    if limit > 0:
        data =data[:limit] 
    for d in data:
        print(f"{d['name']} {d['model']} {d['power']} {d['location']}")

show_all(devices)
              



name = input("设备名称：")
model = input("型号：")
power = float(input("功率："))
location = input("车间：")

device = {
    "name": name,
    "model": model,
    "power": power,
    "location": location
}
devices.append(device)

for key,value in device.items():
    print(f"{key}:{value}")

with open("devices.json","w",encoding="utf-8") as fout:
    json.dump(devices,fout,ensure_ascii=False,indent=2)

with open("devices.json","r",encoding="utf-8") as fin:
    check = json.load(fin)
print(f"现在共 {len(check)} 台")
