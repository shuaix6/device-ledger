devices = ["数控机床","工业机器人","传送带","检测仪","包装机"]
for d in devices:
    print(d)

for i in range(5):
    print(i)

total = 0 
for i in range(1,101):
    total = total + i
print(total)

#============================

devices = ["数控机床","工业机器人","传送带","检测仪","包装机"]

count = 1
for d in devices:
    print(str(count)+ "." + d)
    count = count + 1

print(devices[4])