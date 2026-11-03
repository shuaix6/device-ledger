import json

print("=== 1 · 接住 vs 不接住 ===")


def boom():
    return int("你好")


try:
    print("A 调用前")
    boom()
    print("B 这行永远不执行")
except ValueError as e:
    print("C 接住了：", e)
print("D 接住之后，程序继续往下跑")

print()
print("=== 2 · 类型接错 = 接不住 ===")
try:
    try:
        int("你好")
    except KeyError:
        print("这条永远不会执行")
except ValueError as e:
    print("内层没接住，外层接住了 ->", type(e).__name__, ":", e)

print()
print("=== 3 · 万能 except 的代价 ===")
for bad in ["你好", None, [1, 2]]:
    try:
        int(bad)
    except:
        print("  出错了（但 except 后面没写类型，说不出是什么错）")
    try:
        int(bad)
    except Exception as e:
        print("  写 as e 就知道 ->", type(e).__name__, ":", e)

print()
print("=== 4 · 四块的执行顺序 ===")


def check(x):
    try:
        r = int(x)
    except ValueError:
        print("  except 跑了")
        return None
    else:
        print("  else 跑了，值 =", r)
        return r
    finally:
        print("  finally 跑了")


print("  -- 传好值 '25' --")
check("25")
print("  -- 传坏值 '你好' --")
check("你好")

print()
print("=== 5 · 真实场景：文件不在 ===")
try:
    with open("不存在的文件.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError as e:
    print("  文件找不到 ->", e)

print()
print("=== 6 · 真实场景：JSON 格式坏了 ===")
try:
    json.loads('{"name": "数控机床",}')
except json.JSONDecodeError as e:
    print("  格式错 ->", type(e).__name__, ":", e)

print()
print("=== 7 · 不写 try 的话，第 1 个实验会长什么样 ===")
print("（下面这行真的会炸，所以注释掉；你可以自己取消注释试）")
print('  boom()   ->   Traceback ... ValueError: invalid literal for int() with base 10: \'你好\'')
