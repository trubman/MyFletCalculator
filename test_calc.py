import pytest
from calc import Calculator


class TestCalculators:

    @pytest.mark.parametrize(
        'operation,num1,num2,expectations',
        [
            pytest.param('add', 2, 2, 4, id='add'),
            pytest.param('substract', 2, 2, 0, id='substract'),
            pytest.param('multiply', 2, 2, 4, id='multiply'),
            pytest.param('divide', 2, 2, 1, id='divide'),
            pytest.param('power', 2, 3, 8, id='power'),
            pytest.param('square_root', 25, 2, 5, id='square_root'),
        ]
    )
    def test_standart_operations(self, operation, num1, num2, expectations):
        calc = Calculator()

        result = calc.__getattribute__(operation).__call__(num1, num2)

        assert result == expectations

    @pytest.mark.parametrize(
        'operation,num1,num2,expectations',
        [
            pytest.param('divide', 2, 0,
                         "На ноль делить нельзя! (Во всяком случае в этом калькуляторе)\n",
                         id='divide'),
            pytest.param('square_root', -25, 2,
                         "Брать корень из отрицательного числа мы Вам не позволим!\n",
                         id='square_root'),
        ]
    )
    def test_standart_operations_error(self, operation, num1, num2, expectations, capsys):
        calc = Calculator()

        result = calc.__getattribute__(operation).__call__(num1, num2)
        result_print = capsys.readouterr().out

        assert result_print == expectations

