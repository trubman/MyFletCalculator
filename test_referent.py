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
        expected_print = ("Введите математическое выражение (через пробел):\n"
                          "(Доступные операции: +, -, *, /, **, sqr)\n")
        input_value = '2 + 2'
        monkeypatch.setattr('builtins.input', lambda: input_value)

        result = Referent.get_mathematical_expression()
        result_print = capsys.readouterr().out

        assert (expected_print, input_value) == (result_print, result)

    def test_get_mathematical_expression(self, capsys):
        input_value = '2 + 2'
        input_result = 4
        expected_print = f"{input_value} = {input_result}\n"

        Referent.get_expression_result()
        result_print = capsys.readouterr().out

        assert expected_print == result_print


