# 我猜：重新读回来时，是几台？最后一台是什么？____

import json

# 第 1 步 · 读：把台账拿进来
with open("devices.json","r",encoding="utf-8") as fin:
    data = json.load(fin)
    print("加之前：",len(data),"台")

# 第 2 步 · 改：加一台新设备（就手拼一个同款字典）
new_device = {"name":"自动分拣臂","model":"AS-500","power":6.0,"location":"2号车间"}
data.append(new_device)

# 第 3 步 · 写回：保存（写回原文件！）
with open("devices.json","w",encoding="utf-8") as fout:
    json.dump(data,fout,ensure_ascii=False,indent=4)

# 第 4 步 · 验证：重新读回来数一数
with open("devices.json","r",encoding="utf-8") as fin:
    data2 = json.load(fin)
    
print("加之后：",len(data2),"台")
print("最后一台：", data2[-1])