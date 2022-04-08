from typing import Any, Dict, List
from django.db.models.query import QuerySet
from .utils import operators
from .types import QuerySetOperations

from django.db.models import Q
import json
import re


def add_mui_filters(
    query_set: QuerySet,
    mui_filter_model: str,
    column_field_mappings: Dict[str, str] | None = None,
) -> QuerySet:
    # TODO: Maybe queue + FIFO is quicker?
    _mui_filter_model: Dict[List, str] = json.loads(mui_filter_model)
    link_operator: str | None = _mui_filter_model.get("linkOperator", None)
    filters: List = _mui_filter_model["items"]

    using_or_linker = link_operator == "or" and len(filters) > 1

    if using_or_linker:
        query_set = add_mui_filters_or_linker(query_set, filters, column_field_mappings)
    else:
        query_set = add_mui_filters_and_linker(query_set, filters, column_field_mappings)

    return query_set


def add_mui_filters_or_linker(query_set: QuerySet, filters: List, column_field_mappings: Dict[str, str] | None) -> QuerySet:
    q_objects = Q()
    for filter in filters:
        dict_filter, query_set_operation = read_filter(filter, column_field_mappings)
        if dict_filter is None:
            continue

        if query_set_operation == QuerySetOperations.FILTER:
            q_objects |= Q(**dict_filter)
        else:
            q_objects |= ~Q(**dict_filter)

    query_set = query_set.filter(q_objects)

    return query_set

    
def add_mui_filters_and_linker(query_set: QuerySet, filters: List, column_field_mappings: Dict[str, str] | None) -> QuerySet:
    for filter in filters:
        dict_filter, query_set_operation = read_filter(filter, column_field_mappings)
        if dict_filter is None:
            continue
                    
        if query_set_operation == QuerySetOperations.FILTER:
            query_set = query_set.filter(**dict_filter)
        else:
            query_set = query_set.exclude(**dict_filter)   

    return query_set


def read_filter(dict_filter: Dict, column_field_mappings: Dict[str, str] | None) -> tuple[dict[str, Any], QuerySetOperations]:
    column_name: str = dict_filter["columnField"]
    mui_operator: str = dict_filter["operatorValue"]
    value: str = dict_filter.get("value", None)

    if column_field_mappings is None or column_name not in column_field_mappings:
        column_name = convert_to_snake_case(column_name)

    django_operator, operation_type, possible_val = operators[mui_operator]

    if possible_val is not None:
        value = possible_val

    # If no operation applied
    if value is None or value == "":
        return None, operation_type

    dict_key = '{0}__{1}'.format(column_name, django_operator)

    return {dict_key: value}, operation_type


def convert_to_snake_case(camel_case_field_name: str) -> str:
    snake_case_text = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_field_name).lower()
    return snake_case_text