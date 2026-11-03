# ===== 设备铭牌信息卡 =====
device_name = "数控机床 CNC-850"
model = "CNC-850"
rated_power = 15.5
in_warranty = False

warranty_text = "在保" if in_warranty else "已过保"

print("===== 设备铭牌 =====")
print("设备名称：" + device_name)
print("设备型号：" + model)
print("额定功率：" + str(rated_power) + " kW")
print("保修状态：" + warranty_text)
print("====================")