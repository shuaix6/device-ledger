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
        return "401: key 不对，或者根本没带上"
    if code == 402:
        return "402: 账户余额不足，去充值"
    if code == 429:
        return "429: 请求太频繁，等几十秒再试"
    return f"没预料到的状态码：{code}"


def ask(question, timeout=30):
    """问模型一句话。成功返回回答文字，失败返回一句人话。"""
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": question}
        ]
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
    # 1 正常一条
    print("1 正常")
    print(ask("用一句话解释什么是RAG"))

    # 2 超时：timeout 压到 0.001 秒，必然等不到
    print("\n2 超时")
    print(ask("什么是HTTP", timeout=0.001))

    # 3 key 写错：临时把身份换掉，跑完立刻改回来
    print("\n3 key 错")
    HEADERS["Authorization"] = "Bearer sk-wrong"
    print(ask("什么是HTTP"))
    HEADERS["Authorization"] = f"Bearer {key}"

    # 4 余额不足/限流：不联网，直接把数字喂给 explain_status
    print("\n4 余额不足/限流")
    print(explain_status(402))
    print(explain_status(429))
