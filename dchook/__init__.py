from .webhook import Webhook, send
from importlib.metadata import version

__version__ = f"dchook v{version('dchook')}"

__all__ = [
    "Webhook",
    "send",
    "__version__"
]