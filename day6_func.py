# ===== 实验一：定义与调用 =====
# def say_hello():
#     print("你好！欢迎使用设备管理系统")


# say_hello()
# say_hello()

# ===== 实验二：参数 =====
# def greet(name):
#     print("你好，" + name +"!")

# greet("数控机床")
# greet("工业机器人")
# greet("巡检员老张")
# greet("666")
# greet()

# # ===== 实验三：return（交还结果） =====
# def add(a,b):
#     return a + b

# result = add(3,5)
# print("第一次：" + str(result))

# total = add(result,100)
# print("第二次：" + str(total))

# # ===== 实验四：print 版为什么"接不住" =====
# def add_bad(a,b):
#     print(a + b)

# x = add_bad(3,5)
# print("x是什么？","x是个啥")

# ===== 实验五：return 会"立即结束"函数 =====
def check_temp(temp):
    print("开始检查......")
    if temp > 90:
        return "高温警告！"
        print("这行永远执行不到")
    print("检查完成")
    return "温度正常"

print(check_temp(95))
print(check_temp(70))