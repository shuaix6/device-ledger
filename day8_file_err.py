try:
    f = open("devices.txt","r",encoding="utf-8")
    content = f.read()
    print(content)
    f.close()

except FileNotFoundError as e:
    print("文件没找到——请检查文件名，或者它是否在这个文件夹里。")
    print("详情：", e)
