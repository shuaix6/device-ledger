import json
with open("devices.json","r",encoding="utf-8") as f:
    devices = json.load(f)

while True:
    query = input("请输入设备名称（输入exit）退出：")

    if query == "exit":
        print("再见")
        break

    if query == "":
        continue

    found = False

    for device in devices:
        if query in device["name"]:
            print(device["name"], device["model"], device["power"], device["location"])
            found = True

    if found == False:
        print("没找到：" + query)
