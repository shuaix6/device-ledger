while True:
    try:
        number = int(input("请输入一个数字："))
        break
    except ValueError as e:
        print("请输入正确的类型（数字），请重新输入一个数字：")

print("你输入的数字是：",number)