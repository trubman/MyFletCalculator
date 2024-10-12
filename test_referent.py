import sys
import pytest
from referent import Referent

class TestReferentWorks:

    # я понимаю, что это тестирование встроенных функций, но я ведь еще учусь
    def test_get_value_from_input(self, monkeypatch):
        input_value = '5'
        monkeypatch.setattr('builtins.input', lambda: input_value)
        result = Referent.get_input()
        assert input_value == result

    # я понимаю, что это тестирование встроенных функций, но я ведь еще учусь
    def test_get_value_from_output(self, capsys):
        input_value = '5'
        expected = f'{input_value}\n'
        Referent.do_output(input_value)
        captured = capsys.readouterr()
        result = captured.out
        assert expected == result

    def test_get_mathematical_expression(self, monkeypatch, capsys):
        expected = ""
        input_value = '2 + 2'
        monkeypatch.setattr('builtins.input', lambda: input_value)
        Referent.get_mathematical_expression()
        captured = capsys.readouterr()
        result = captured.out
        assert expected == result


