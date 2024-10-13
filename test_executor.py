import pytest
from executor import Executor


class TestExecutorWorks:

    @pytest.mark.parametrize(
        "incoming,result,expected", [
            pytest.param("12 + 12", 24, "12 + 12 = 24\n", id='12 + 12 = 24'),
            pytest.param("", None, "", id='None'),
        ]
    )
    def test_get_outgoing(self, incoming, result, expected, capsys):
        exe = Executor()
        exe.cleaned_incoming = incoming
        exe.result = result

        exe.get_outgoing()
        result_print = capsys.readouterr().out

        assert expected == result_print

    @pytest.mark.parametrize(
        "incoming,expected,first,expected_print", [
            pytest.param("  12 + 12  ", "12 + 12", True,
                         "Введите математическое выражение (операторы и операнды через пробел):\n"
                         "(Доступные операции: +, -, *, /, **, sqr)\n", id='"  12 + 12  "'),
            pytest.param("  12 + 12  ", "12 + 12", False,
                         "", id='first=False'),
            pytest.param(24, "24 + 0", False,
                         "24 - не является строкой\n", id='24 int'),
        ]
    )
    def test_set_cleaned_values(self, incoming, expected, first, expected_print, monkeypatch, capsys):
        exe = Executor()
        count = True
        monkeypatch.setattr('builtins.input', lambda: incoming)
        try:
            result = exe.set_cleaned_values(first)
            result_print = capsys.readouterr().out
        except RecursionError:
            monkeypatch.setattr('builtins.input', lambda: '24 + 0')
            result = exe.set_cleaned_values(first)
            result_print = expected_print
        assert (result_print, result) == (expected_print, expected)

    @pytest.mark.parametrize(
        "cleaned_incoming,expected,first,expected_print", [
            pytest.param("12 + 12", [12, 'add', 12], False,
                         "", id='good'),
            pytest.param("12+12", [], True,
                         "Выражение 12+12 - недопустимо\n"
                         "Введите математическое выражение (операторы и операнды через пробел):\n"
                         "(Доступные операции: +, -, *, /, **, sqr)\n", id='bad'),
        ]
    )
    def test_set_splited_values(self, cleaned_incoming, expected, first, expected_print, capsys, monkeypatch):
        exe = Executor()
        exe.cleaned_incoming = cleaned_incoming
        try:
            exe.set_splited_values()
        except OSError:
            monkeypatch.setattr('builtins.input', lambda: '12 + 12')
        result = exe.splited_incoming
        result_print = capsys.readouterr().out

        assert (result_print, result) == (expected_print, expected)

    @pytest.mark.parametrize(
        "splited_incoming,incoming,expected,expected_print", [
            pytest.param([12, 'add', 12], '12 + 12', 24,
                         "", id="[12, 'add', 12]"),
            pytest.param([12, 'divide', 0], '12 / 0', False,
                         "На ноль делить нельзя! (Во всяком случае в этом калькуляторе)\n"
                         "¯\_(ツ)_/¯ - мои полномочия все...\n",
                         id="[12, 'divide', 0]"),
            pytest.param([-1, 'square_root', 2], '-1 sqr', False,
                         "Брать корень из отрицательного числа мы Вам не позволим!\n"
                         "¯\_(ツ)_/¯ - мои полномочия все...\n",
                         id="[-1, 'square_root', 2]"),
        ]
    )
    def test_do_math(self, splited_incoming, incoming, expected, expected_print, capsys):
        exe = Executor()
        exe.cleaned_incoming = incoming
        exe.splited_incoming = splited_incoming
        result = exe.do_math()
        result_print = capsys.readouterr().out
        assert (result_print, result) == (expected_print, expected)

