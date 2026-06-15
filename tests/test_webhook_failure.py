from unittest.mock import patch, Mock
import pytest

from dchook import send


@patch("dchook.webhook.requests.post")
def test_send_failure(mock_post):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.text = "Bad Request"

    mock_post.return_value = mock_response

    with pytest.raises(Exception):
        send(
            "https://discord.com/api/webhooks/test",
            "Hello"
        )