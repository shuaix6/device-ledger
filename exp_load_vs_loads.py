import json

print("=== 同一批数据，三种形态 ===")

print("\n【形态 1】硬盘上的文件里，长这样：")
with open("devices.json", "r", encoding="utf-8") as f:
    s = f.read()
print(s[:110])

print("\n【形态 2】读到内存里，是一串字符串，长这样：")
print(repr(s[:60]))
print("类型：", type(s), " 长度：", len(s), "个字符")

print("\n【形态 3】解析成 Python 对象，长这样：")
d = json.loads(s)
print(d[0])
print("类型：", type(d), " 元素个数：", len(d))

print()
print("=== 形态 1 和 2 是同一批字符吗 ===")
print("是的——文件里存的就是这串字符，read 只是把它搬进内存")
print("所以 load(f) 和 loads(s) 拿到的原材料完全一样")

print()
print("=== 两个函数只是入口不同 ===")
with open("devices.json", "r", encoding="utf-8") as f:
    a = json.load(f)
b = json.loads(s)
print("load(f)  的结果：", type(a), len(a), "条")
print("loads(s) 的结果：", type(b), len(b), "条")
print("两者相等？", a == b)

print()
print("=== 反过来：dumps 把对象变回字符串 ===")
one = {"name": "数控机床", "power": 15.5}
text = json.dumps(one, ensure_ascii=False)
print("原字典：      ", one)
print("dumps 之后：  ", text)
print("类型：        ", type(text))
back = json.loads(text)
print("loads 回来：  ", back)
print("和原字典相等？", one == back)

print()
print("=== 四兄弟的 2x2 ===")
print("              读进来(JSON->Python)   写出去(Python->JSON)")
print("  文件        json.load(f)           json.dump(d, f)")
print("  字符串      json.loads(s)          json.dumps(d)")

print()
print("=== 什么时候手上有字符串（而不是文件）===")
resp_text = '{"status": "ok", "count": 4}'
print("模拟接口返回的文本：", resp_text, "  类型：", type(resp_text))
obj = json.loads(resp_text)
print("loads 之后：", obj, "  类型：", type(obj))
print("能按键取值了：obj['count'] =", obj["count"])
