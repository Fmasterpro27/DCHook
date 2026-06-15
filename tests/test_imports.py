import dchook


def test_version_exists():
    assert hasattr(dchook, "__version__")


def test_exports_exist():
    assert hasattr(dchook, "Webhook")
    assert hasattr(dchook, "send")