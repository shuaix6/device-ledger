count = 1

while count <= 5:
    print(count)
    count = count + 1

print("循环结束")

# ===== 实验三：input 第一次交互 =====
name = input("请输入设备名称：")
print("你输入的设备是："+ name)

# ===== 实验四：input 的数字陷阱 =====
num = input("请输入一个数字：")
print(int(num) + 1)
