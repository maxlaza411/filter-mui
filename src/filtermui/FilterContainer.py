from typing import Any, Dict, List

from django.db.models.query import QuerySet

from django.db.models import Q
from .filter_types import QuerySetOperations


class FilterContainer:
    def __init__(self, orgin_queryset: QuerySet, using_or_linker: bool) -> None:
        self.using_or_linker = using_or_linker
        self.orgin_queryset = orgin_queryset

        if using_or_linker:
            self.q_objects = Q()

    def __iadd__(self, filter_input: tuple[dict[str, Any], QuerySetOperations, callable | None]) -> None:
        dict_filter = filter_input[0]
        query_set_operation = filter_input[1]
        run_cond = filter_input[2]

        if run_cond:
            run_cond(self.orgin_queryset)

        if self.using_or_linker:
            if query_set_operation == QuerySetOperations.FILTER:
                if isinstance(dict_filter, Q):
                    self.q_objects |= dict_filter
                else:
                    self.q_objects |= Q(**dict_filter)
            else:
                if isinstance(dict_filter, Q):
                    self.q_objects |= ~dict_filter
                else:
                    self.q_objects |= ~Q(**dict_filter)
        else:
            if query_set_operation == QuerySetOperations.FILTER:
                if isinstance(dict_filter, Q):
                    self.orgin_queryset = self.orgin_queryset.filter(dict_filter)
                else:
                    self.orgin_queryset = self.orgin_queryset.filter(**dict_filter)
            else:
                if isinstance(dict_filter, Q):
                    self.orgin_queryset = self.orgin_queryset.exclude(dict_filter)
                else:
                    self.orgin_queryset = self.orgin_queryset.exclude(**dict_filter)

    def __call__(self) -> QuerySet:
        if self.using_or_linker:
            self.orgin_queryset = self.orgin_queryset.filter(self.q_objects)

        return self.orgin_queryset