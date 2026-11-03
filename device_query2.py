# 产出 2.0 · 设备查询（数据从文件来）
# 我猜在文件夹里找某台设备的详细数据

devices = []

try:
    f = open("devices.txt","r",encoding="utf-8")
    for line in f:
        parts = line.strip().split(",")
        device = {
            "name":parts[0],
            "model":parts[1],
            "power":parts[2],
            "location":parts[3],
        }
        devices.append(device)
    f.close()
except FileNotFoundError as e:
    print("数据文件没找到——请确认 devices.txt在这个文件夹里。")
    print("详情：", e)
    exit()

print("设备台账加载完成，共",len(devices),"台")


while True:
    query = input("请输入设备名称（输入exit退出）：")
    if query == "exit":
        print("再见")
        break
    found = False
    for device in devices:
        if query in device["name"]:
            print("名称：",device["name"])
            print("型号：",device["model"])
            print("功率：",device["power"])
            print("位置：",device["location"])
            found = True
    if not found:
        print("没找到:",query)
    