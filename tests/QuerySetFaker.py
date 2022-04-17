from __future__ import annotations

from typing import Any, List, TypeVar


_QS = TypeVar("_QS", bound="QuerySetFaker")


class QuerySetFaker:
    def __init__(self) -> None:
        self.called_functions: List[dict] = []

    def filter(self: _QS, *args: Any, **kwargs: Any) -> QuerySetFaker:
        self.called_functions.append({"type": "filter", "args": args, "kwargs": kwargs})

        return self

    def exclude(self: _QS, *args: Any, **kwargs: Any) -> QuerySetFaker:
        self.called_functions.append(
            {"type": "exclude", "args": args, "kwargs": kwargs}
        )

        return self
