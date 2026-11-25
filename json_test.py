import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("DEEPSEEK_KEY")

URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"
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


def ask_json(question, timeout=30):
    """问模型一句话，要求它返回 JSON，解析成字典交出去。"""
    system_text = (
        "你必须输出 JSON，格式为 "
        + '{"answer": "回答内容", "confidence": 0 到 1 的小数}。'
        + "不要输出任何其他内容，不要加代码块标记。"
        + "answer 只用一句话说完，不要分点、不要编号、不要列举步骤。"
    )
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_text},
            {"role": "user", "content": question}
        ],
        "temperature": 0,
        "response_format": {"type": "json_object"}
    }

    try:
        r = requests.post(URL, headers=HEADERS, json=data, timeout=timeout)
    except requests.exceptions.Timeout:
        return {"error": f"超时：等了 {timeout} 秒"}
    except requests.exceptions.ConnectionError:
        return {"error": "连不上：检查网络，或者地址写错了"}

    trouble = explain_status(r.status_code)
    if trouble:
        return {"error": trouble}

    try:
        text = r.json()["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError):
        return {"error": "取内容失败", "raw": r.text[:200]}

    try:
        return json.loads(text)
    except ValueError:
        return {"error": "解析失败", "raw": r.text[:200]}


question = "轴承温度过高怎么办"

ok = 0
for i in range(10):
    result = ask_json(question)
    if "error" in result:
        print(i + 1, "✗", result.get("error"),
              "|", str(result.get("raw", ""))[:60])
    else:
        ok += 1
        answer = str(result.get("answer", ""))
        print(i + 1, "✓", answer, "| confidence =", result.get("confidence"))

print()
print(f"成功 {ok}/10")
