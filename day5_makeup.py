# ===== 补课 1：and / or / not =====
temperature = 95
fault_count = 4

# and：两个都成立才为真（"而且"）
if temperature > 90 and fault_count > 3:
    print("双重警报:高温 + 故障频繁")

# or：有一个成立就为真（"或者"）
if temperature > 100 or fault_count > 10:
    print("(这行不会打印)")
else:
    print("(or 检查：两个条件都没到线)")

# not：把结果反过来（"非"）
in_warranty = True
if not in_warranty:
    print("已过保")
else:
    print("（not 检查：还在保）")

# ===== 补课 2：% 取模 =====
print(10 % 3)
print(8 % 2)
print(7 % 2)

# 经典用法：判断奇偶
n = 7
if n % 2 == 0:
    print("偶数")
else:
    print("奇数")

# ===== 补课 3：列表按索引修改 =====
devices = ["数控机床","工业机器人","传送带"]
devices[1] = "焊接机器人"
print(devices)
