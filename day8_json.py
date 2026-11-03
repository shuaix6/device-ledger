# 我猜：json.load 读出来的 data，type() 会是什么？（列表 / 字典 / 字符串？）
#列表装字典

import json

f = open("devices.json","r",encoding="utf-8")
data = json.load(f)
f.close()

print(data)
print(type(data))
print(len(data))

total = 0
for device in data:
    print(device["name"],"·功率",device["power"],"kW")
    total = total + device["power"]

print("——")
print("设备总数：",len(data),"台")
print("总功率：",total,"kW")
