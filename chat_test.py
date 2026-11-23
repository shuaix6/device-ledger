import os

import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("DEEPSEEK_KEY")

URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"
HEADERS = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}


def explain_status(code):
    """ 把 HTTP 状态码翻译成人话。200 表示没问题，返回空字符串。"""
    if code == 200:
        return ""
    if code == 401:
        return "401: key 不对， 或者根本没带上"
    if code == 402:
        return "402: 账户余额不足， 去充值"
    if code == 429:
        return "429: 请求太频繁，等几十秒再试"
    return f"没预料到的状态码：{code}"


def ask_chat(messages, timeout=30):
    """把整段对话发出去，返回模型这一句回复；失败返回None。"""
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0,
    }
    try:
        r = requests.post(URL, headers=HEADERS, json=data, timeout=timeout)
    except requests.exceptions.Timeout:
        print(f" [失败]超时：等了 {timeout}秒")
        return None
    except requests.exceptions.ConnectionError:
        print("  [失败] 连不上：检查网络")
        return None
    except requests.exceptions.RequestException as e:
        print(f"  [失败] 请求异常：{e}")
        return None

    trouble = explain_status(r.status_code)
    if trouble:
        print(f" [失败] {trouble}")
        return None

    try:
        return r.json()["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError):
        print(f" [失败] 取内容失败：{r.text[:200]}")
        return None


messages = [{"role": "system", "content": "你是一个设备维修工程师，回答简短。"}]

print("输入问题开始聊，输入 quit 退出。\n")

try:
    while True:
        q = input(f"你问（已带 {len(messages)} 条历史）：").strip()

        if q == "quit":
            break
        if q == "":
            continue

        reply = ask_chat(messages + [{"role": "user", "content": q}])
        if reply is None:
            continue

        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": reply})

        print(f"\n模型: {reply}\n")
except KeyboardInterrupt:
    print()

print("对话结束，历史共", len(messages), "条。")
