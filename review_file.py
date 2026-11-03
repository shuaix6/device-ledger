try:
    with open("devices.txt","r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError as e:
    print("文件不存在")
    print("详情：", e)
finally:
    print("—— 无论如何，门已关 ——")
    