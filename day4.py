devices = ["数控机床","工业机器人","传送带","检测仪","包装机"]

print(devices[0])
print(devices[2])
print(devices[-1])
print(devices[-2])

print(len(devices))


devices.append("激光切割机")
print(devices)
print(len(devices))

devices.remove("传送带")
print(devices)
print(len(devices))

print(devices.append("激光切割机"))