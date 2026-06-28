"""Epicidiom package."""

__all__ = ["greeting"]


def greeting(name: str = "world") -> str:
    """Return a friendly greeting."""
    clean_name = name.strip() or "world"
    return f"Hello, {clean_name}!"
