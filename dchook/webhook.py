import requests


class Webhook:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, content: str):
        payload = {
            "content": content
        }

        response = requests.post(
            self.webhook_url,
            json=payload,
            timeout=10
        )

        if response.status_code not in (200, 204):
            raise Exception(
                f"Failed to send message: {response.status_code} - {response.text}"
            )

        return True


def send(webhook_url: str, content: str):
    """
    Send a message to a Discord webhook.

    Parameters:
        webhook_url (str): Discord webhook URL.
        content (str): Message content.
    """
    webhook = Webhook(webhook_url)
    return webhook.send(content)