# 实验九 · 逐行读
#我猜不出来

f = open("devices.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()


print("----读完了----")