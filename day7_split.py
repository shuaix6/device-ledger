# 实验十二 · 切分（一行拆成几块）
# 我猜按逗号一行打成串

f = open("devices.txt","r",encoding="utf-8")
for line in f:
    parts = line.strip().split(",")
    print(parts)
f.close()

print("----读完了----")