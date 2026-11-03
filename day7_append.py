# 实验八 · 追加模式
# 跑这个来给文件追加内容

f = open("my_devices.txt","a",encoding="utf-8")
f.write("机器人手臂\n")
f.close()

print("追加完成")
