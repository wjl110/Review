# -*- coding: utf-8 -*-
"""Unit tests for app_gradio helper functions (no real API calls)."""
import os
import sys

# Provide a dummy key so the module-level OpenAI client can be instantiated
# without a real credential – tests mock the client before any network call.
os.environ.setdefault("DASHSCOPE_API_KEY", "test-key-placeholder")

# Ensure Proj/ is importable when running from repo root
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


def test_history_to_messages_empty():
    """Empty history produces an empty messages list."""
    from app_gradio import _history_to_messages

    assert _history_to_messages([]) == []
    assert _history_to_messages(None) == []


def test_history_to_messages_dict_format():
    """Gradio 6 dict-style history is converted correctly."""
    from app_gradio import _history_to_messages

    history = [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"},
    ]
    result = _history_to_messages(history)
    assert result == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"},
    ]


def test_history_to_messages_list_format():
    """Old-style [user, assistant] tuple history is converted correctly."""
    from app_gradio import _history_to_messages

    history = [["hello", "hi"]]
    result = _history_to_messages(history)
    assert result == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"},
    ]


def test_history_to_messages_skips_none_entries():
    """None entries in old-style history are skipped."""
    from app_gradio import _history_to_messages

    history = [[None, "assistant only"]]
    result = _history_to_messages(history)
    assert result == [{"role": "assistant", "content": "assistant only"}]


def test_chat_empty_message_returns_unchanged_history():
    """chat() with blank input returns current history unchanged."""
    from unittest.mock import MagicMock, patch

    mock_client = MagicMock()
    with patch("app_gradio.client", mock_client):
        from app_gradio import chat

        history = [{"role": "user", "content": "previous"}]
        result_history, result_msg = chat("   ", history)
        assert result_history == history
        assert result_msg == ""
        mock_client.chat.completions.create.assert_not_called()


def test_clear_chat():
    """clear_chat() resets both chatbot history and input box."""
    from app_gradio import clear_chat

    history, msg = clear_chat()
    assert history == []
    assert msg == ""
