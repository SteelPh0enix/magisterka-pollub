from typing import Any


def value_or_default(value: Any | None, default: Any) -> Any:
    return value if value is not None else default
