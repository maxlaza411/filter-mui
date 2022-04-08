from typing import Callable, List
from .QuerySetFaker import QuerySetFaker
from ..filtermui import add_mui_filters
from .data import json_string_two, json_string_one, json_string_three

import unittest


class TestFilterMUI(unittest.TestCase):
    def test_example_one(self):
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_one)
        self.assertEqual([{'type': 'filter', 'args': (), 'kwargs': {'timeout_id__icontains': 'de'}}], faker.called_functions)

    def test_example_two():
        # w/o and/or prompt
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_two)


    def test_example_three():
        faker = QuerySetFaker()
        add_mui_filters(faker, json_string_three)
