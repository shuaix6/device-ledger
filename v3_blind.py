import json

FILE = "devices.json"

def load_devices():
    with open(FILE,"r",encoding="utf-8") as fin:
        return json.load(fin)

def save_devices(devices):
    with open(FILE,"w",encoding="utf-8") as fout:
        json.dump(devices,fout,ensure_ascii=False,indent=2)

def print_one(d):
    print(f"{d['id']} {d['name']} {d['model']} {d['power']} {d['location']}")

def show_all(devices):
    for d in devices:
        print_one(d)
    print(f"共 {len(devices)} 台")

def find_by_name(devices):
    keyword = input("要查什么名字：")
    if keyword == "": 
        print("名字不能为空")
        return
    
    found = False
    for d in devices:
        if keyword in d["name"]:
            print_one(d)
            found = True
    if not found:
        print("没有这个设备")    

def find_by_location(devices):
    keyword = input("要查哪个车间：")
    if keyword == "":
        print("车间不能为空")
        return

    found = False
    for d in devices:
        if keyword in d["location"]:
            print_one(d)
            found = True
    if not found:
        print("没有匹配")

def add_devices(devices):
    name = input("请输入新设备名称：")
    model = input("请输入新设备型号：")
    try:
        power = float(input("请输入新设备功率："))
    except ValueError:
        print("请输入数字")
        return
    location = input("请输入新设备车间：")

    dup = False
    for d in devices:
        if d["name"] == name and d["model"] == model:
            dup = True
    if dup:
        print("这台设备已经在了，没有重复添加")
        return
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
    save_devices(devices)
    print(f"已添加，id是{new_id}")

def delete_devices(devices):
    try:
        target =int(input("要删除哪个id:"))
    except ValueError:
        print("id必须是数字")
        return

    found = None
    for d in devices:
        if d["id"] == target:
            found = d

    if found is None:
        print(f"没有id是 {target} 的设备 ")
        return

    print(f"确认删除 {found['id']} 号 {found['name']} {found['model']}的设备吗")
    confirm = input("确认删除输入 y ，其他取消：")

    if confirm != "y":
        return

    devices.remove(found)
    save_devices(devices)
    print("已删除")

def edit_power(devices):
    try:
        target =int(input("要改哪个id的功率:"))
    except ValueError:
        print("id必须是数字")
        return

    found = None
    for d in devices:
        if d["id"] == target:
            found = d

    if found is None:
        print(f"没有id是 {target} 的设备 ")
        return

    print(f"当前 {found['name']},功率{found['power']}")
    try:
        new_power = float(input("新功率是："))
    except ValueError:
        print("请输入数字，取消修改")
        return

    found["power"] = new_power
    save_devices(devices)
    print("已修改")



def main():
    devices = load_devices()
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
            show_all(devices)

        elif choice == "0":
            print("已退出")
            break

        elif choice == "2":
            find_by_name(devices)
        
        elif choice == "3":
            find_by_location(devices)

        elif choice == "4":
            add_devices(devices)

        elif choice == "5":
            delete_devices(devices)

        elif choice == "6":
            edit_power(devices)


        else:
            print("这项功能还没做")

main()
