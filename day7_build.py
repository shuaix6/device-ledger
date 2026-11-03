# 实验十三 · 列表装字典（组装"一台台"设备）
#我猜：我没猜到

# devices = []

# f = open("devices.txt","r", encoding="utf-8")
# for line in f:
#     parts = line.strip().split(",")
#     device = {
#         "name": parts[0],
#         "model":parts[1],
#         "power":parts[2],
#         "location":parts[3],
#     }
#     devices.append(device)
# f.close()

# print(devices)








# devices = []

# f =open("devices.txt","r",encoding="utf-8")
# for line in f:
#     parts = line.strip().split(",")
#     device = {
#         "name":parts[0],
#         "model":parts[1],
#         "power":parts[2],
#         "location":parts[3],
#     }
#     devices.append(device)
# f.close()

# print(devices)












devices = []
f = open("devices.txt","r",encoding="utf-8")
for line in f:
    parts = line.strip().split(",")
    device = {
        "name":parts[0],
        "model":parts[1],
        "power":parts[2],
        "location":parts[3],
    }
    devices.append(device)
f.close()

print(devices)
