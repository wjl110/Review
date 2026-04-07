# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 注意: 不同地域的base_url不通用（下方示例使用新加坡地域的base_url）
# - 新加坡: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
# - 华北2（北京）: https://dashscope.aliyuncs.com/compatible-mode/v1
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)
completion = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[{"role": "user", "content": "你是谁？"}]
)
print(completion.choices[0].message.content)
