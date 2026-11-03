f = open("devices.txt","r",encoding="utf-8")

try:
    content = f.read()
    print(content)
finally:
    f.close()
    print("—— 无论如何，门已关 ——")
