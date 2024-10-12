import sys
import pytest
from referent import get_input

class TestReferentWorks:

    def test_get_value_from_input(self, monkeypatch):
        input_value = '5'
        monkeypatch.setattr('builtins.input', lambda: input_value)
        result = get_input()
        assert input_value == result