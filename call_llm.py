import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("DEEPSEEK_KEY")

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization":f"Bearer {key}",
    "Content-Type":"application/json"
}
data = {
    "model": "deepseek-flash",
    "messages":[
        {"role": "user", "content":"用一句话解释什么是RAG"}
    ]
}

r = requests.post(url,headers=headers,json=data)
print("状态码：",r.status_code)
print(r.json())