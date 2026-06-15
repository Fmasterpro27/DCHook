from unittest.mock import patch, Mock

from dchook import send


@patch("dchook.webhook.requests.post")
def test_send_message(mock_post):
    mock_response = Mock()
    mock_response.status_code = 204

    mock_post.return_value = mock_response

    result = send(
        "https://discord.com/api/webhooks/test",
        "Hello"
    )

    assert result is True