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

    elif choice == "4":
        name = input("设备名：")
        model = input("型号：")
        try:
            power = float(input("功率："))
        except ValueError:
            print("功率必须是数字，这次新增取消")
            continue
        location = input("车间：")

        dup = False
        for d in devices:
            if d["name"] == name and d["model"] == model:
                dup = True
        if dup:
            print("这台设备已经在了，没有重复添加")
            continue

        max_id = 0
        for d in devices:
            if d["id"] > max_id:
                max_id = d["id"]
        new_id = max_id + 1

        devices.append({
            "id": new_id,
            "name": name,
            "model": model,
            "power": power,
            "location": location 
        })

        with open("devices.json","w",encoding="utf-8") as fout:
            json.dump(devices,fout,ensure_ascii=False,indent=2)

        print(f"已添加，id是{new_id}")

    elif choice == "5":
        try:
            target  = int(input("要删哪个 id: "))
        except ValueError:
            print("id 必须是整数")
            continue

        found = None
        for d in devices:
            if d["id"] == target:
                found = d

        if found is None:
            print(f"没有 id 为{target} 的设备")
            continue

        print(f"确认删除 {found['id']} 号 {found['name']} {found['model']} 吗？")
        confirm = input("输入 y 确认，其他取消：")

        if confirm != "y":
            print("已取消")
            continue

        devices.remove(found)

        with open("devices.json","w",encoding="utf-8") as fout:
            json.dump(devices,fout,ensure_ascii=False,indent=2)

        print("已删除")

    elif choice == "6":
        try:
            target = int(input("要改哪个 id 的功率："))
        except ValueError:
            print("id 必须是整数")
            continue

        found = None
        for d in devices:
            if d["id"] == target:
                found = d 

        if found is None:
            print(f"没有 id 为 {target} 的设备")
            continue

        print(f"当前：{found['name']},功率 {found['power']}")
        try:
            new_power = float(input("新功率是多少："))
        except ValueError:
            print("功率必须是数字，这次修改取消")
            continue
        
        found["power"] = new_power

        with open("devices.json", "w", encoding="utf-8") as fout:
            json.dump(devices, fout, ensure_ascii=False, indent=2)

        print("已修改")

  
    elif choice == "0":
        print("再见，退出")
        break
    else:
        print("这个功能还没做")