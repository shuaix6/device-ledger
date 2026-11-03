# 我猜：套壳后输入"你好"，程序会运行结束  
try:
    number = int(input("请输入一个数字："))
    print("你输入的数字是：",number)
except ValueError as e:    
    print("这好像不是数字——请重跑一次，输入数字（比如31）。")
    print("出错详情：",e)

print("---程序跑完了---")
