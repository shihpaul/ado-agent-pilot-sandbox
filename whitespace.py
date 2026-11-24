"""Utilities for normalizing whitespace."""


def normalize_whitespace(text: str) -> str:
    """Trim whitespace and replace each internal whitespace run with a space."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return " ".join(str.split(text))
