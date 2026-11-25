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
        return "401: key 不对， 或者根本没带上"
    if code == 402:
        return "402: 账户余额不足， 去充值"
    if code == 429:
        return "429: 请求太频繁，等几十秒再试"
    return f"没预料到的状态码：{code}"


def ask(question, system=None, examples=None, timeout=30):
    """问模型一句话。

    system   : 角色设定，不给就是普通对话
    examples : 例题列表，每个元素形如{"q": 问，"a": 答}
    """
    messages = []
    if system:
        messages.append({"role": "system", "content": system})

    if examples:
        for ex in examples:
            messages.append({"role": "user", "content": ex["q"]})
            messages.append({"role": "assistant", "content": ex["a"]})

    messages.append({"role": "user", "content": question})

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0
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

    examples = [
        {
            "q": "电机运行时有异响怎么办",
            "a": "1. 立即停机断电\n2. 检查轴承是否磨损\n3. 检查联轴器对中"
        },
        {
            "q": "减速机油位过低怎么办",
            "a": "1. 停机检查是否漏油\n2. 补同牌号润滑油至标准油位\n3. 记录补油量并观察一周"
        },
        {
            "q": "空压机排气温度高怎么办",
            "a": "1. 检查冷却水流量\n2. 清理散热器积灰\n3. 检查润滑油是否变质"
        },
    ]

    print("========== A 版：不给例子 ==========")
    print(ask(question))

    print()
    print("========== B 版：给 3 个例子 ==========")
    print(ask(question, examples=examples))
