import pytest
from referent import get_input

class TestReferentWorks:

    def test_get_value_from_input(self):
        input_value = '5'
        result = get_input(input_value)
        assert input_value == result