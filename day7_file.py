#实验六 · 第一次读文件 
#我猜：会把txt里的44行字打印出来
f = open("device_info.txt","r",encoding="utf-8")
content = f.read()
f.close()

print(content)
print("---- 读取完成 ----")