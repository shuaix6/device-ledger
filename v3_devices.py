import json

with open("devices.json","r",encoding="utf-8") as fin:
    devices = json.load(fin)

while True:
    print("==== 设备台账 ====")
    print("1. 查看全部设备")
    print("2. 按名称查")   
    print("3. 按车间查")
    print("4. 新增设备")
    print("5. 删除设备")
    print("6. 修改功率")
    print("0. 退出")

    choice = input("请选择：")

    if choice == "1":
        for d in devices:
            print(f"{d['id']} {d['name']} {d['model']} {d['power']} {d['location']}")
        print(f"共 {len(devices)} 台")

    elif choice == "2":
        keyword = input("要查什么名字：")
        if keyword == "":
            print("名字不能为空")
            continue
        found = False
        for d in devices:
            if keyword in d["name"]:
                print(f"{d['id']} {d['name']} {d['model']} {d['power']} {d['location']}")
                found = True
        if not found:
            print("没有匹配")
    
    elif choice == "3":
        keyword = input("要查什么车间：")
        if keyword == "":
            print("车间不能为空")
            continue
        found = False
        for d in devices:
            if keyword in d["location"]:
                print(f"{d['id']} {d['name']} {d['model']} {d['power']} {d['location']}")
                found = True
        if not found:
            print("没有匹配")
            
    
    elif choice == "0":
        print("再见，退出")
        break
    else:
        print("这个功能还没做")