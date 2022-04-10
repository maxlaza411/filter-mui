from tests import (
    QuerySetFaker,
    json_string_two,
    json_string_one,
    json_string_three,
    json_string_four,
    json_string_five,
)
from src.filtermui import add_mui_filters

import unittest


class TestFilterMUI(unittest.TestCase):
    def test_example_one(self):
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_one, {"MRN": "medical_record_number"})
        self.assertEqual(
            [
                {
                    "type": "filter",
                    "args": (),
                    "kwargs": {"timeout_completed__iexact": True},
                },
                {
                    "type": "filter",
                    "args": (),
                    "kwargs": {"medical_record_number__icontains": "ffre"},
                },
                {
                    "type": "filter",
                    "args": (),
                    "kwargs": {"patient_name__iendswith": "Bob"},
                },
            ],
            faker.called_functions,
        )

    def test_example_two(self):
        # w/o and/or prompt
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_two)
        self.assertEqual(
            "[{'type': 'filter', 'args': (<Q: (OR: ('first_name__iendswith', 'd'), ('indication_for_drug__isnull', "
            "True))>,), 'kwargs': {}}]",
            str(faker.called_functions),
        )

    def test_example_three(self):
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_three)
        self.assertEqual(
            [
                {
                    "type": "filter",
                    "args": (),
                    "kwargs": {"timeout_completed__iexact": True},
                },
                {"type": "filter", "args": (), "kwargs": {"status__icontains": "xds"}},
            ],
            faker.called_functions,
        )

    def test_example_four(self):
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_four, {"Bob": "Bob"})
        self.assertEqual(
            [
                {
                    "type": "filter",
                    "args": (),
                    "kwargs": {"timeout_completed__iexact": True},
                }
            ],
            faker.called_functions,
        )

    def test_example_five(self):
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_five)
        self.assertEqual(
            [
                {
                    "type": "filter",
                    "args": (),
                    "kwargs": {"timeout_completed__iexact": True},
                }
            ],
            faker.called_functions,
        )


# TODO: Possible Speedup here. query = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue":
#  "is", "value": true }, { "columnField": "status", "id": 3467, "operatorValue": "contains" } ], "linkOperator":
#  "or" }' faker = QuerySetFaker() qs = add_mui_filters(faker, query) faker.called_functions [{'type': 'filter',
#  'args': (<Q: (AND: ('timeout_completed__iexact', True))>,), 'kwargs': {}}]
