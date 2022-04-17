import json
import re
from typing import Any, Dict, List

from django.db.models import Q
from django.db.models.query import QuerySet

from .django_filter_operators import operators
from .filter_types import QuerySetOperations


def add_mui_filters(
    query_set: QuerySet,
    mui_filter_model: str,
    column_field_mappings: Dict[str, str] | None = None,
) -> QuerySet:
    _mui_filter_model: Dict[List, str] = json.loads(mui_filter_model)
    link_operator: str | None = _mui_filter_model.get("linkOperator", None)
    filters: List = _mui_filter_model["items"]

    using_or_linker = link_operator == "or" and len(filters) > 1

    # Nicer way to do this?
    if using_or_linker:
        # Lot of slow down with "or"
        q_objects = Q()
        for filter in filters:
            dict_filter, query_set_operation = read_filter(
                filter, column_field_mappings
            )
            if dict_filter is None:
                continue

            if query_set_operation == QuerySetOperations.FILTER:
                q_objects |= Q(**dict_filter)
            else:
                q_objects |= ~Q(**dict_filter)

        query_set = query_set.filter(q_objects)
    else:
        for filter in filters:
            dict_filter, query_set_operation = read_filter(
                filter, column_field_mappings
            )
            if dict_filter is None:
                continue

            if query_set_operation == QuerySetOperations.FILTER:
                query_set = query_set.filter(**dict_filter)
            else:
                query_set = query_set.exclude(**dict_filter)

    return query_set


def read_filter(
    dict_filter: Dict, column_field_mappings: Dict[str, str] | None
) -> tuple[dict[str, Any], QuerySetOperations] | tuple[None, QuerySetOperations]:
    column_name: str = dict_filter["columnField"]
    mui_operator: str = dict_filter["operatorValue"]
    value: str = dict_filter.get("value", None)

    if column_field_mappings is None or column_name not in column_field_mappings:
        column_name = convert_to_snake_case(column_name)
    else:
        column_name = column_field_mappings[column_name]

    django_operator, operation_type, possible_val = operators[mui_operator]

    if possible_val is not None:
        value = possible_val

    # If no operation applied
    if value is None or value == "":
        return None, operation_type

    dict_key = "{0}__{1}".format(column_name, django_operator)

    return {dict_key: value}, operation_type


def convert_to_snake_case(camel_case_field_name: str) -> str:
    snake_case_text = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_case_field_name).lower()
    return snake_case_text
