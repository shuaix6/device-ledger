# 我猜：输错的时候，程序会让我继续输入，直到exit结束

while True:
    try:
        number=int(input("请输入一个数字："))
        break
    except ValueError as e:
        print("这好像不是数字——请再输一次。")

print("你输入的数字是：",number)
print("----程序跑完了---")
