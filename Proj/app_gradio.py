# -*- coding: utf-8 -*-
"""
使用 Gradio 构建的本地 Web UI，调用阿里云百炼通义千问 API。
"""
import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
MODEL = "qwen3.5-plus"


def _history_to_messages(history: list) -> list:
    """把 Chatbot 的 history 转成 API 用的 messages（Gradio 6 为 list[dict]）。"""
    out = []
    for h in history or []:
        if isinstance(h, dict) and "role" in h:
            out.append({"role": h["role"], "content": h.get("content", "") or ""})
        elif isinstance(h, (list, tuple)) and len(h) >= 2:
            if h[0]:
                out.append({"role": "user", "content": str(h[0])})
            if h[1]:
                out.append({"role": "assistant", "content": str(h[1])})
    return out


def chat(message: str, history: list) -> tuple[list, str]:
    """单轮对话：发用户消息给模型，返回 Gradio 6 格式的 history（list[dict]）并清空输入框。"""
    if not message.strip():
        return history or [], ""
    messages = _history_to_messages(history)
    messages.append({"role": "user", "content": message})
    try:
        completion = client.chat.completions.create(model=MODEL, messages=messages)
        reply = completion.choices[0].message.content or ""
        # Gradio 6 Chatbot 的 value = list[{"role","content"}]
        return messages + [{"role": "assistant", "content": reply}], ""
    except Exception as e:
        return history or [], str(e)


def clear_chat():
    return [], ""


with gr.Blocks(title="通义千问 · 本地对话") as demo:
    gr.Markdown("## 通义千问 (Qwen3.5-Plus)\n基于阿里云百炼 API 的本地对话 Demo")
    chatbot = gr.Chatbot(label="对话", height=400)
    msg = gr.Textbox(
        label="输入",
        placeholder="输入消息后按 Enter 发送…",
        show_label=False,
        container=False,
    )
    with gr.Row():
        submit_btn = gr.Button("发送", variant="primary")
        clear_btn = gr.Button("清空")

    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    submit_btn.click(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear_btn.click(clear_chat, outputs=[chatbot, msg])

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, theme=gr.themes.Soft())
