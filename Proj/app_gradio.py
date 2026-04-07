# -*- coding: utf-8 -*-
"""
使用 Gradio 构建的本地 Web UI，调用阿里云百炼通义千问 API。
"""
import os
import logging
from typing import List, Dict, Tuple, Union, Optional
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import gradio as gr

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

# 验证 API Key
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    logger.error("DASHSCOPE_API_KEY environment variable is not set")
    raise ValueError("DASHSCOPE_API_KEY environment variable is required")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
MODEL = "qwen3.5-plus"


def _history_to_messages(history: Optional[List[Union[Dict, Tuple, List]]]) -> List[Dict[str, str]]:
    """
    把 Chatbot 的 history 转成 API 用的 messages（Gradio 6 为 list[dict]）。

    Args:
        history: Gradio Chatbot 的对话历史，可以是 dict 或 tuple/list 格式

    Returns:
        转换后的消息列表，格式为 [{"role": "user/assistant", "content": "..."}]
    """
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


def chat(message: str, history: Optional[List]) -> Tuple[List[Dict[str, str]], str]:
    """
    单轮对话：发用户消息给模型，返回 Gradio 6 格式的 history（list[dict]）并清空输入框。

    Args:
        message: 用户输入的消息
        history: 当前对话历史

    Returns:
        更新后的对话历史和空字符串（用于清空输入框）
    """
    if not message.strip():
        return history or [], ""

    # 输入验证：限制消息长度
    max_length = 10000
    if len(message) > max_length:
        error_msg = f"消息长度超过限制（最大 {max_length} 字符）"
        logger.warning(f"Message too long: {len(message)} characters")
        return history or [], error_msg

    messages = _history_to_messages(history)
    messages.append({"role": "user", "content": message})

    try:
        logger.info(f"Sending message to API, conversation length: {len(messages)}")
        completion = client.chat.completions.create(model=MODEL, messages=messages)
        reply = completion.choices[0].message.content or ""
        logger.info(f"Received response from API, length: {len(reply)}")
        # Gradio 6 Chatbot 的 value = list[{"role","content"}]
        return messages + [{"role": "assistant", "content": reply}], ""
    except OpenAIError as e:
        error_msg = f"API 调用错误: {str(e)}"
        logger.error(f"OpenAI API error: {e}")
        return history or [], error_msg
    except Exception as e:
        error_msg = f"未知错误: {str(e)}"
        logger.error(f"Unexpected error in chat: {e}", exc_info=True)
        return history or [], error_msg


def clear_chat() -> Tuple[List, str]:
    """
    清空对话历史和输入框。

    Returns:
        空的对话历史列表和空字符串
    """
    logger.info("Clearing chat history")
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
