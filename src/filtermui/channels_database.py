from typing import Any

from channels.db import database_sync_to_async
from django.db.models import Q
from django.db.models.query import QuerySet


@database_sync_to_async
def run_filter(query_set: QuerySet, dict_filter: dict[str, Any] | Q):
    return query_set.filter(**dict_filter)


@database_sync_to_async
def run_exclude(query_set: QuerySet, dict_filter: dict[str, Any] | Q):
    return query_set.exclude(**dict_filter)