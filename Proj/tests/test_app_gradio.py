"""
Unit tests for app_gradio.py
"""
import pytest
from unittest.mock import patch, MagicMock
from openai import OpenAIError


def test_history_to_messages_with_dict_format(sample_history):
    """
    测试将字典格式的历史记录转换为消息列表
    """
    from app_gradio import _history_to_messages

    result = _history_to_messages(sample_history)

    assert len(result) == 2
    assert result[0]["role"] == "user"
    assert result[0]["content"] == "你好"
    assert result[1]["role"] == "assistant"
    assert result[1]["content"] == "你好！有什么我可以帮助你的吗？"


def test_history_to_messages_with_tuple_format(sample_history_tuple_format):
    """
    测试将元组格式的历史记录转换为消息列表
    """
    from app_gradio import _history_to_messages

    result = _history_to_messages(sample_history_tuple_format)

    assert len(result) == 4
    assert result[0]["role"] == "user"
    assert result[0]["content"] == "你好"
    assert result[1]["role"] == "assistant"
    assert result[2]["role"] == "user"
    assert result[3]["role"] == "assistant"


def test_history_to_messages_with_empty_history():
    """
    测试空历史记录的处理
    """
    from app_gradio import _history_to_messages

    result = _history_to_messages(None)
    assert result == []

    result = _history_to_messages([])
    assert result == []


def test_history_to_messages_with_mixed_format():
    """
    测试混合格式的历史记录处理
    """
    from app_gradio import _history_to_messages

    mixed_history = [
        {"role": "user", "content": "第一条消息"},
        ("第二条用户消息", "第二条助手回复"),
    ]

    result = _history_to_messages(mixed_history)

    assert len(result) == 3
    assert result[0]["content"] == "第一条消息"
    assert result[1]["content"] == "第二条用户消息"
    assert result[2]["content"] == "第二条助手回复"


@pytest.mark.parametrize("message,expected_length", [
    ("你好", 1),
    ("", 0),
    ("   ", 0),
])
def test_chat_with_empty_or_whitespace_message(message, expected_length):
    """
    测试空消息或纯空格消息的处理
    """
    from app_gradio import chat

    history = []
    result_history, result_input = chat(message, history)

    if expected_length == 0:
        assert result_history == []
        assert result_input == ""


@patch('app_gradio.client')
def test_chat_successful_response(mock_client, sample_history, mock_env_vars):
    """
    测试成功的对话响应
    """
    from app_gradio import chat

    # Mock the API response
    mock_completion = MagicMock()
    mock_completion.choices = [MagicMock()]
    mock_completion.choices[0].message.content = "这是 AI 的回复"
    mock_client.chat.completions.create.return_value = mock_completion

    message = "新的问题"
    result_history, result_input = chat(message, sample_history)

    # Check that the history was updated correctly
    assert len(result_history) == 4  # 2 original + 1 user + 1 assistant
    assert result_history[-2]["role"] == "user"
    assert result_history[-2]["content"] == "新的问题"
    assert result_history[-1]["role"] == "assistant"
    assert result_history[-1]["content"] == "这是 AI 的回复"
    assert result_input == ""


@patch('app_gradio.client')
def test_chat_with_openai_error(mock_client, sample_history, mock_env_vars):
    """
    测试 OpenAI API 错误的处理
    """
    from app_gradio import chat

    # Mock an API error
    mock_client.chat.completions.create.side_effect = OpenAIError("API 调用失败")

    message = "测试消息"
    result_history, result_input = chat(message, sample_history)

    # History should remain unchanged
    assert result_history == sample_history
    # Error message should be returned in the input field
    assert "API 调用错误" in result_input


@patch('app_gradio.client')
def test_chat_with_generic_exception(mock_client, sample_history, mock_env_vars):
    """
    测试通用异常的处理
    """
    from app_gradio import chat

    # Mock a generic exception
    mock_client.chat.completions.create.side_effect = Exception("意外错误")

    message = "测试消息"
    result_history, result_input = chat(message, sample_history)

    # History should remain unchanged
    assert result_history == sample_history
    # Error message should be returned
    assert "未知错误" in result_input


def test_chat_message_length_validation(mock_env_vars):
    """
    测试消息长度验证
    """
    from app_gradio import chat

    # Create a message that exceeds the limit
    long_message = "a" * 10001  # Exceeds max_length of 10000

    result_history, result_input = chat(long_message, [])

    # Should return empty history
    assert result_history == []
    # Should return error message
    assert "消息长度超过限制" in result_input


def test_clear_chat():
    """
    测试清空对话功能
    """
    from app_gradio import clear_chat

    result_history, result_input = clear_chat()

    assert result_history == []
    assert result_input == ""


@patch('app_gradio.client')
def test_chat_with_none_history(mock_client, mock_env_vars):
    """
    测试 history 为 None 的情况
    """
    from app_gradio import chat

    # Mock the API response
    mock_completion = MagicMock()
    mock_completion.choices = [MagicMock()]
    mock_completion.choices[0].message.content = "AI 回复"
    mock_client.chat.completions.create.return_value = mock_completion

    message = "你好"
    result_history, result_input = chat(message, None)

    # Should create new history
    assert len(result_history) == 2  # user + assistant
    assert result_history[0]["role"] == "user"
    assert result_history[1]["role"] == "assistant"
