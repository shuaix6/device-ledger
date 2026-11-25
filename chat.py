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


def ask(question, timeout=30):
    """问一句，返回回答文字；失败返回 None（原因 call_llm 已打印）。"""
    return call_llm([{"role": "user", "content": question}], timeout=timeout)


def ask_json(question, timeout=30):
    """问一句，要求模型返回 JSON，解析成字典；失败返回 {"error": ...}。"""
    system_text = (
        "你必须输出 JSON，格式为 "
        + '{"answer": "回答内容", "confidence": 0 到 1 的小数}。'
        + "不要输出任何其他内容，不要加代码块标记。"
        + "answer 只用一句话说完，不要分点、不要编号、不要列举步骤。"
    )
    msgs = [
        {"role": "system", "content": system_text},
        {"role": "user", "content": question},
    ]
    text = call_llm(msgs, json_mode=True, timeout=timeout)
    if text is None:
        return {"error": "请求失败，具体原因看上面的提示"}
    try:
        return json.loads(text)
    except ValueError:
        return {"error": "解析失败", "raw": text[:200]}


def chat(system_text="你是一个设备维修工程师，回答简短。"):
    """多轮对话：问一句、答一句，历史累积。输入 quit 退出，返回整段历史。"""
    messages = [{"role": "system", "content": system_text}]

    print("输入问题开始聊，输入 quit 退出。\n")

    try:
        while True:
            q = input(f"你问（已带 {len(messages)} 条历史）：").strip()

            if q == "quit":
                break
            if q == "":
                continue

            reply = call_llm(messages + [{"role": "user", "content": q}])
            if reply is None:
                continue

            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": reply})

            with open("run.log", "a", encoding="utf-8") as f:
                f.write(f"问：{q}\n")
                f.write(f"答：{reply}\n\n")

            print(f"\n模型: {reply}\n")
    except KeyboardInterrupt:
        print()

    print("对话结束，历史共", len(messages), "条。")
    return messages


if __name__ == "__main__":
    print("1 ask")
    print(ask("用一句话解释什么是RAG"))

    print("\n2 ask_json")
    print(ask_json("轴承温度过高怎么办"))

    print("\n3 chat")
    chat()
