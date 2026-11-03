import json

print("=== 场景 1：接口返回的文本（3 周后你会天天遇到）===")
resp_text = '{"code": 0, "data": {"devices": [{"name": "数控机床", "power": 15.5}, {"name": "焊接机器人", "power": 8.2}]}}'
print("拿到的东西类型：", type(resp_text))

obj = json.loads(resp_text)
print("loads 之后类型：", type(obj))
print("一层层取：obj['data']['devices'][0]['name'] =", obj["data"]["devices"][0]["name"])
print("第二台功率：", obj["data"]["devices"][1]["power"])

print()
print("=== 用 load 干同样的事会怎样 ===")
try:
    json.load(resp_text)
except AttributeError as e:
    print("load 报错 ->", e)
    print("原因：load 第一步要调 .read()，字符串没这个方法")

print()
print("=== 场景 2：日志文件，每行一整条 JSON ===")
log_lines = [
    '{"time": "10:01", "level": "INFO", "msg": "启动"}',
    '{"time": "10:02", "level": "ERROR", "msg": "读文件失败"}',
    '这行不是 JSON，是普通文字',
    '{"time": "10:03", "level": "INFO", "msg": "重试成功"}',
]
for line in log_lines:
    try:
        rec = json.loads(line)
        print("  ", rec["time"], rec["level"], rec["msg"])
    except json.JSONDecodeError:
        print("   （跳过一行非 JSON 内容）")

print()
print("=== 场景 3：自己 dumps 出来的字符串，再 loads 回去 ===")
original = {"name": "传送带", "power": 3.0}
text = json.dumps(original, ensure_ascii=False)
print("dumps ->", text, type(text))
print("loads ->", json.loads(text), " 相等？", original == json.loads(text))

print()
print("=== 对比：文件里的 JSON 该怎么读 ===")
print("笨办法（多一步）：")
with open("devices.json", "r", encoding="utf-8") as f:
    a = json.loads(f.read())
print("   json.loads(f.read()) ->", len(a), "条")
print("直接（load 内部就是干这个）：")
with open("devices.json", "r", encoding="utf-8") as f:
    b = json.load(f)
print("   json.load(f)        ->", len(b), "条")
print("结果一样吗？", a == b)
