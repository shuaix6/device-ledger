# 实验七 · 第一次写文件
# 我猜：______________________________________
# （提示：注意屏幕——三行设备名会出现吗？）

f = open("my_devices.txt","w",encoding="utf-8")
f.write("数控机床\n")
f.write("焊接机器人")
f.write("传送带\n")
f.close()

print("写完了")