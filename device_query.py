# ===== 产出：设备信息查询脚本 =====
device = {
    "name":"数控机床 CNC-850",
    "model":"CNC-850",
    "power":15.5,
    "location":"车间 A",
}

while True:
    key = input("查什么信息？（name / model / power / location,输入 exit 退出）：")
    if key == "exit":
        break
    if key in device:
        print("查询结果:" + str(device[key]))
    else:
        print("没有这个信息，请检查后重试")

print("已退出查询。")
