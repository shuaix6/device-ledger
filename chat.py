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


def call_llm(messages, json_mode=False, timeout=30):
    """把整段对话发给大模型，返回这一句回复的文字；失败返回 None。"""
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0,
    }
    if json_mode:
        data["response_format"] = {"type": "json_object"}

    try:
        r = requests.post(URL, headers=HEADERS, json=data, timeout=timeout)
    except requests.exceptions.Timeout:
        print(f"[失败] 超时：等了 {timeout} 秒")
        return None
    except requests.exceptions.ConnectionError:
        print("[失败] 连不上：检查网络")
        return None
    except requests.exceptions.RequestException as e:
        print(f"[失败] 请求异常：{e}")
        return None

    trouble = explain_status(r.status_code)
    if trouble:
        print(f"[失败] {trouble}")
        return None

    try:
        return r.json()["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError):
        print(f"[失败] 取内容失败：{r.text[:200]}")
        return None


if __name__ == "__main__":
    msgs = [{"role": "user", "content": "用一句话解释什么是RAG"}]
    print("1 普通模式")
    print(call_llm(msgs))

    print("\n2 json 模式")
    msgs2 = [
        {"role": "system", "content": '输出 JSON, 格式 {"answer": "一句话回答"}'},
        {"role": "user", "content": "什么是RAG"},
    ]
    print(call_llm(msgs2, json_mode=True))
