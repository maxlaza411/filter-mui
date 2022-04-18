import unittest

from src.filtermui import add_mui_filters
from tests import (
    QuerySetFaker,
    JSON_STRING_FIVE,
    JSON_STRING_FOUR,
    JSON_STRING_ONE,
    JSON_STRING_THREE,
    JSON_STRING_TWO,
)


class TestFilterMUI(unittest.TestCase):
    """
    Test class for filtermui program
    """

    def test_example_one(self):
        """Test number one"""
        faker = QuerySetFaker()
        add_mui_filters(faker, JSON_STRING_ONE, {"MRN": "medical_record_number"})
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
        """Test number two"""
        # w/o and/or prompt
        faker = QuerySetFaker()
        add_mui_filters(faker, JSON_STRING_TWO)
        self.assertEqual(
            "[{'type': 'filter', 'args': (<Q: (OR: ('first_name__iendswith', 'd'), ('indication_for_drug__isnull', "
            "True))>,), 'kwargs': {}}]",
            str(faker.called_functions),
        )

    def test_example_three(self):
        """Test number three"""
        faker = QuerySetFaker()
        add_mui_filters(faker, JSON_STRING_THREE)
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
        """Test number 4"""
        faker = QuerySetFaker()
        add_mui_filters(faker, JSON_STRING_FOUR, {"Bob": "Bob"})
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
        """Test number five"""
        faker = QuerySetFaker()
        add_mui_filters(faker, JSON_STRING_FIVE)
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
