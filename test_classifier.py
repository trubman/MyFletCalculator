from ast import Param

import pytest
from classifier import Classifier


class TestClassifierWorks:

    @pytest.mark.parametrize(
        "input_str,expected", [
            pytest.param("  2 + 2  ", "2 + 2", id='"  2 + 2  " -> "2 + 2"'),
            pytest.param("SQR", "sqr", id='SQR -> sqr'),
        ]
    )
    def test_do_clean_input_func(self, input_str, expected):
        cls = Classifier()

        result = cls.do_clean_input(input_str)

        assert expected == result

    def test_do_clean_input_error(self, capsys):
        input_str = 2 + 2
        expected = f"{input_str} - не является строкой\n"
        cls = Classifier()

        cls.do_clean_input(input_str)
        result_print = capsys.readouterr().out

        assert expected == result_print

    @pytest.mark.parametrize(
        "input_str,expected", [
            pytest.param('2 + 2', [2, 'add', 2], id="[2, '+', 2]"),
            pytest.param('2 - 2', [2, 'substract', 2], id="[2, '-', 2]"),
            pytest.param('2 * 2', [2, 'multiply', 2], id="[2, '*', 2]"),
            pytest.param('2 / 2', [2, 'divide', 2], id="[2, '/', 2]"),
            pytest.param('2 ** 2', [2, 'power', 2], id="[2, '**', 2]"),
            pytest.param('sqr 2', ['square_root', 2, 2], id="['sqr', 2]"),
            pytest.param('1 + 22 - 333 * 4444 ** 55555',
                         [1, 'add', 22, 'substract', 333, 'multiply', 4444, 'power', 55555],
                         id="[1, '+', 22, '-', 333, '*', 4444, '**', 55555]"),
        ]
    )
    def test_check_input_func(self, input_str, expected):
        cls = Classifier()

        result = cls.check_input(input_str)

        assert result == expected


