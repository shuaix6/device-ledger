import json

print("=== A · loads 吃字符串 ===")
a = json.loads('{"name": "数控机床", "power": 15.5}')
print(a)
print(type(a))

print()
print("=== B · load 吃文件 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    b = json.load(f)
print(type(b), "共", len(b), "条")
print(b[0])

print()
print("=== C · 搞混会怎样 ===")
try:
    json.load('{"a": 1}')
except Exception as e:
    print("json.load(字符串)  ->", type(e).__name__, ":", e)

print()
print("=== D · with 正常走完 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    json.load(f)
print("f.closed =", f.closed)

print()
print("=== E · with 中途炸 ===")
try:
    with open("devices.json", "r", encoding="utf-8") as f2:
        1 / 0
except ZeroDivisionError:
    print("炸了：division by zero")
print("f2.closed =", f2.closed)

print()
print("=== F · 老写法中途炸（对照）===")
f3 = open("devices.json", "r", encoding="utf-8")
try:
    json.load(f3)
    1 / 0
except ZeroDivisionError:
    print("炸了：division by zero")
print("f3.closed =", f3.closed, "  <-- 没关")
f3.close()

print()
print("=== G · 文件关了，数据还在吗 ===")
try:
    f2.read()
except Exception as e:
    print("f2.read()  ->", type(e).__name__, ":", e)
print("但读出来的数据照样用：b[0] =", b[0])
