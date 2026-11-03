while True:
    try:
        n = int(input("请输入一个数字:"))
        break
    except ValueError as e:
        print("这不是数字,请重新输入")

print("你输入的数字是:"n)
