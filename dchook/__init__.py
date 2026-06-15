from .webhook import Webhook, send
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = f"dchook v{version('dchook')}"
except PackageNotFoundError:
    __version__ = "dchook dev"

__all__ = [
    "Webhook",
    "send",
    "__version__"
]