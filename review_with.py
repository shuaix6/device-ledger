# #----实验A
# with open("devices.txt","r",encoding="utf-8") as f:
#     print(f.read())

# print("关了吗？",f.closed)

#实验B
try:
    with open("devices.txt","r",encoding="utf-8") as f:
        print(f.read())
        number = int("这不是数字")
except ValueError as e:
    print("接住了：",e)
    print("这时关了吗？",f.closed)
