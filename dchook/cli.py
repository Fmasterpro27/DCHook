import argparse
import os
import sys

from .webhook import send
from importlib.metadata import version

__version__ = version("dchook")


def main():
    parser = argparse.ArgumentParser(
        prog="dchook",
        description="Send messages to Discord webhooks."
    )

    parser.add_argument(
    "-v",
    "-V",
    "--version",
    action="version",
    version=f"dchook v{__version__}"
    )

    parser.add_argument(
        "message",
        help="Message to send."
    )

    parser.add_argument(
        "-w",
        "--webhook",
        help="Discord webhook URL."
    )

    args = parser.parse_args()

    webhook_url = args.webhook or os.getenv("DCHOOK_WEBHOOK")

    if not webhook_url:
        print(
            "Error: No webhook URL provided.\n"
            "Use --webhook or set DCHOOK_WEBHOOK.",
            file=sys.stderr
        )
        sys.exit(1)

    try:
        send(
            webhook_url=webhook_url,
            content=args.message
        )

        print("✓ Message sent successfully.")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()