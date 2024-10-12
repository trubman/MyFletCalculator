import sys
import pytest
from referent import get_input, get_output

class TestReferentWorks:

    def test_get_value_from_input(self, monkeypatch):
        input_value = '5'
        monkeypatch.setattr('builtins.input', lambda: input_value)
        result = get_input()
        assert input_value == result

    def test_get_value_from_output(self, capsys):
        input_value = '5'
        expected = '5\n'
        get_output(input_value)
        captured = capsys.readouterr()
        result = captured.out
        assert expected == result
