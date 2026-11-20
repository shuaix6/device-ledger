import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("DEEPSEEK_KEY")

if key is None or key.strip() == "":
    print("没读到 key。检查 .env 文件里 DEEPSEEK_KEY= 后面有没有填东西")
elif not key.startswith("sk-"):
    print(f"读到了，但格式不对：开头是 {key[:6]}，应该以 sk- 开头")
elif key != key.strip():
    print("读到了，但首尾有多余空格，去掉就好")
else:
    print("读到了，格式正常")
    print(f"  长度：{len(key)}")
    print(f"  开头：{key[:6]}")
    print(f"  结尾：{key[-4:]}")
    print("（中间部分故意不打印，防止泄露）")
