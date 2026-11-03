devices = []

f = open("devices.txt","r", encoding="utf-8")
for line in f:
    parts = line.strip().split(",")
    device = {
        "name": parts[0],
        "model":parts[1],
        "power":parts[2],
        "location":parts[3],
    }
    devices.append(device)
f.close()

query = input("请输入设备名称：")

for device in devices:
    if device["name"] == query:
        print(device)