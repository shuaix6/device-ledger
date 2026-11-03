# 我猜：输入"你好"的时候，else 不出现

try:
    number = int(input("请输入一个数字："))
except ValueError:
    print("这不是数字——试试输入32这样的")
else:
    print("没出意外！数字是：",number)
