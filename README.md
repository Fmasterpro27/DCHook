# DCHook

> A lightweight Python library and CLI for sending messages through Discord webhooks.

[![PyPI version](https://img.shields.io/pypi/v/dchook.svg)](https://pypi.org/project/dchook/)
[![Python versions](https://img.shields.io/pypi/pyversions/dchook.svg)](https://pypi.org/project/dchook/)
[![License](https://img.shields.io/pypi/l/dchook.svg)](LICENSE)

---

## Features

- Send messages through Discord webhooks
- Simple Python API
- Command Line Interface (CLI)
- Lightweight and easy to use
- Minimal dependencies
- Fast and reliable
- Python 3.8+

---

## Installation

```bash
pip install dchook
```

---

## Quick Start

```python
from dchook import send

send(
    "YOUR_WEBHOOK_URL",
    "Hello from DCHook!"
)
```

---

## Python API

### Send a Message

```python
from dchook import send

send(
    "YOUR_WEBHOOK_URL",
    "Hello World!"
)
```

### Using the Webhook Class

```python
from dchook import Webhook

hook = Webhook("YOUR_WEBHOOK_URL")

hook.send("Hello World!")
hook.send("Another message!")
```

---

## CLI Usage

### Send a Message

```bash
dchook "Hello World!" -w YOUR_WEBHOOK_URL
```

### Using an Environment Variable

Linux/macOS:

```bash
export DCHOOK_WEBHOOK="YOUR_WEBHOOK_URL"

dchook "Hello World!"
```

Windows PowerShell:

```powershell
$env:DCHOOK_WEBHOOK="YOUR_WEBHOOK_URL"

dchook "Hello World!"
```

### Show Version

```bash
dchook --version
```

---

## Example

```python
from dchook import send

send(
    "https://discord.com/api/webhooks/...",
    "Deployment completed successfully."
)
```

---

## Testing

```bash
pytest
```

---

## Requirements

- Python 3.8+
- requests

---

## License

Apache License 2.0

---

## Author

Developed by **JackMa**

GitHub: https://github.com/Fmasterpro27

---

## Links

- Homepage: https://github.com/Fmasterpro27/DCHook
- Issues: https://github.com/Fmasterpro27/DCHook/issues
- PyPI: https://pypi.org/project/dchook/

---

## License

Licensed under the Apache License 2.0.
