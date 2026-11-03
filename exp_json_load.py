import json

print("=== 1 · f.read() 只给你一串文字 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    raw = f.read()
print("类型：", type(raw))
print("开头 60 个字符长这样：")
print(repr(raw[:60]))

print()
print("=== 2 · json.loads(raw) 把文字变成 Python 对象 ===")
data = json.loads(raw)
print("类型：", type(data), " 共", len(data), "条")
print("第一条：", data[0])

print()
print("=== 3 · json.load(f) 一步做完上面两步 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)
print("类型：", type(data2), " 共", len(data2), "条")

print()
print("=== 4 · 两条路结果一样吗 ===")
print("data == data2 ?", data == data2)

print()
print("=== 5 · 先 read 完，再 load 会怎样 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    first = f.read()
    print("read 拿到了", len(first), "个字符")
    try:
        second = json.load(f)
        print("再 load 拿到：", second)
    except json.JSONDecodeError as e:
        print("再 load 报错 ->", type(e).__name__, ":", e)

print()
print("=== 6 · 文件指针跑到哪了 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    print("刚打开时 tell() =", f.tell())
    f.read()
    print("read 完之后 tell() =", f.tell())

print()
print("=== 7 · 文件有多大 ===")
import os
print("devices.json 字节数：", os.path.getsize("devices.json"))
