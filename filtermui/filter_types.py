from enum import Enum
from typing import TypedDict


class QuerySetOperations:
    FILTER = 0
    EXCLUDE = 1


class OperatorType(TypedDict):
    mui_filter: str
    results: tuple[str, QuerySetOperations, bool | None]
