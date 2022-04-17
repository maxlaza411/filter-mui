from .filter_types import OperatorType, QuerySetOperations

# Note that case does not matter.
operators: OperatorType = {
    "is": ("iexact", QuerySetOperations.FILTER, None),
    "contains": ("icontains", QuerySetOperations.FILTER, None),
    "equals": ("iexact", QuerySetOperations.FILTER, None),
    "startsWith": ("istartswith", QuerySetOperations.FILTER, None),
    "endsWith": ("iendswith", QuerySetOperations.FILTER, None),
    "isEmpty": ("isnull", QuerySetOperations.FILTER, True),
    "isNotEmpty": ("isnull", QuerySetOperations.FILTER, False),
    "not": ("iexact", QuerySetOperations.EXCLUDE, None),
    "after": ("gt", QuerySetOperations.FILTER, None),
    "onOrAfter": ("gte", QuerySetOperations.FILTER, None),
    "before": ("lt", QuerySetOperations.FILTER, None),
    "onOrBefore": ("lte", QuerySetOperations.FILTER, None),
}
