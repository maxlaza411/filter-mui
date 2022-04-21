import json
import re
from typing import Any, Dict, List

from django.db.models.query import QuerySet

from .django_filter_operators import operators
from .filter_types import QuerySetOperations
from .FilterContainer import FilterContainer


def add_mui_filters(
    query_set: QuerySet,
    mui_filter_model: str,
    column_field_mappings=None,
    conditionally_run: dict[str, callable] | None = None
) -> QuerySet:
    _mui_filter_model: Dict[List, str] = json.loads(mui_filter_model)
    link_operator: str | None = _mui_filter_model.get("linkOperator", None)
    filters: List = _mui_filter_model["items"]

    if len(filters) == 0:
        return query_set

    using_or_linker = link_operator == "or" and len(filters) > 1

    generated_filters = FilterContainer(query_set, using_or_linker)
    for filter in filters:
        generated_filter = read_filter(filter, column_field_mappings, conditionally_run)
        
        if not generated_filter[0]:
            continue

        generated_filters += generated_filter

    return generated_filters


def read_filter(
    dict_filter: Dict,
    column_field_mappings,
    conditionally_run: dict[str, callable] | None
) -> tuple[dict[str, Any], QuerySetOperations, bool] | tuple[None, QuerySetOperations, callable | None]:
    column_name: str = dict_filter["columnField"]
    mui_operator: str = dict_filter["operatorValue"]
    value: str = dict_filter.get("value", None)

    if column_field_mappings is None or column_name not in column_field_mappings:
        column_name = convert_to_snake_case(column_name)
    else:
        # Allow function args
        if callable(column_field_mappings[column_name]):
            return column_field_mappings[column_name](column_name, mui_operator, value)

        column_name = column_field_mappings[column_name]

    django_operator, operation_type, possible_val = operators[mui_operator]

    cond_run_res = conditionally_run.get(column_name, None)

    if possible_val is not None:
        value = possible_val

    # If no operation applied
    if value is None or value == "":
        return None, operation_type, cond_run_res

    dict_key = "{0}__{1}".format(column_name, django_operator)

    return {dict_key: value}, operation_type, cond_run_res


def convert_to_snake_case(camel_case_field_name: str) -> str:
    snake_case_text = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_case_field_name).lower()
    return snake_case_text
