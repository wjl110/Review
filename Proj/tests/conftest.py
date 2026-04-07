"""
Test configuration and fixtures for the Proj module tests.
"""
import os
import pytest
from unittest.mock import Mock, MagicMock
from openai import OpenAI


@pytest.fixture
def mock_openai_client(monkeypatch):
    """
    Mock OpenAI client to avoid actual API calls during testing.
    """
    mock_client = Mock(spec=OpenAI)
    mock_completion = MagicMock()
    mock_completion.choices = [MagicMock()]
    mock_completion.choices[0].message.content = "这是一个测试响应"

    mock_client.chat.completions.create.return_value = mock_completion

    # Mock the OpenAI class constructor
    monkeypatch.setattr("openai.OpenAI", lambda **kwargs: mock_client)

    return mock_client


@pytest.fixture
def mock_env_vars(monkeypatch):
    """
    Mock environment variables for testing.
    """
    monkeypatch.setenv("DASHSCOPE_API_KEY", "test_api_key_12345")


@pytest.fixture
def sample_history():
    """
    Sample chat history for testing.
    """
    return [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好！有什么我可以帮助你的吗？"}
    ]


@pytest.fixture
def sample_history_tuple_format():
    """
    Sample chat history in tuple format (Gradio old format).
    """
    return [
        ("你好", "你好！有什么我可以帮助你的吗？"),
        ("介绍一下你自己", "我是通义千问，一个由阿里云开发的大型语言模型。")
    ]
