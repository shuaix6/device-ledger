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


def ask(question, system=None, timeout=30):
    """问模型一句话。成功返回回答文字，失败返回一句人话。"""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": question})

    data = {
        "model": MODEL,
        "messages":  messages
    }

    try:
        r = requests.post(URL, headers=HEADERS, json=data, timeout=timeout)
    except requests.exceptions.Timeout:
        return f"超时：等了 {timeout} 秒，对方一直没回话"
    except requests.exceptions.ConnectionError:
        return "连不上：检查网络，或者地址写错了"

    trouble = explain_status(r.status_code)
    if trouble:
        return trouble

    try:
        return r.json()["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError):
        return "返回的不是预期结构，原始内容：" + r.text[:200]


if __name__ == "__main__":
    question = "轴承温度过高怎么办"

    print("== A 版：不加角色 ==")
    print(ask(question))

    print()
    print("== B 版：加角色 ==")
    role = "你是一名有 20 年经验的工厂设备维修工程师。"
    role += "回答必须给出可执行的检查步骤，按 1. 2. 3. 编号。"
    print(ask(question, system=role))
