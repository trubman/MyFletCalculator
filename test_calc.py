import pytest
from calc import Calculator, AdvancedCalculator


class TestCalculators:

    @pytest.fixture(scope="class")
    def prepare_calculators(self):
        Calc = Calculator()
        AdvCalc = AdvancedCalculator()
        return {'Calc': Calc, 'AdvCalc': AdvCalc}

    @pytest.mark.parametrize(
        'name,value,expectations',
        [
            pytest.param('Calc', ('a', 'b'), "Допустимы только целые числа!\n",
                         id="try input 'a', 'b' in Calc"),
            pytest.param('AdvCalc', ('a', 'b'), "Допустимы только целые числа!\n",
                         id="try input 'a', 'b' in AdvCalc"),
        ]
    )
    def test_set_and_get_value_error_works(self, name, value, expectations, prepare_calculators, capsys):
        """ Проверим функцию set_value() с недопустимыми входными значениями"""
        # GIVEN/ДАНО prepare_calculators, name, value, expectations
        # WHEN/КОГДА
        prepare_calculators[name].set_value(*value)
        captured = capsys.readouterr()
        # THEN/ТОГДА
        assert captured.out == expectations

    @pytest.mark.parametrize(
        'name,value,expectations',
        [
            pytest.param('Calc', (5, 6), "Текущия значения: 5 и 6\n",
                         id="input 5, 6 in Calc"),
            pytest.param('AdvCalc', (5, 6), "Текущия значения: 5 и 6\n",
                         id="input 5, 6 in AdvCalc"),
        ]
    )
    def test_set_and_get_value_normal_works(self, name, value, expectations, prepare_calculators, capsys):
        """ Проверим функцию set_value() """
        # GIVEN/ДАНО prepare_calculators, name, value, expectations
        # WHEN/КОГДА
        prepare_calculators[name].set_value(*value)
        prepare_calculators[name].get_value()
        captured = capsys.readouterr()
        # THEN/ТОГДА
        assert captured.out == expectations

    @pytest.mark.parametrize(
        'name,operation,expectations',
        [
            pytest.param('Calc', 'add', "5 + 6 = 11\n", id="5 + 6 in Calc"),
            pytest.param('AdvCalc', 'add', "5 + 6 = 11\n", id="5 + 6 in AdvCalc"),
            pytest.param('Calc', 'substract', "5 - 6 = -1\n", id="5 - 6 in Calc"),
            pytest.param('AdvCalc', 'substract', "5 - 6 = -1\n", id="5 - 6 in AdvCalc"),
            pytest.param('Calc', 'multiply', "5 * 6 = 30\n", id="5 * 6 in Calc"),
            pytest.param('AdvCalc', 'multiply', "5 * 6 = 30\n", id="5 * 6 in AdvCalc"),
            pytest.param('Calc', 'divide', "5 / 6 = 0.83\n", id="5 / 6 in Calc"),
            pytest.param('AdvCalc', 'divide', "5 / 6 = 0.83\n", id="5 / 6 in AdvCalc"),
        ]
    )
    def test_standart_operations(self, name, operation, expectations, prepare_calculators, capsys):
        """ Проверим выполнение операций в Calc (и у его нследника AdvCalc) """
        # GIVEN/ДАНО name, operation, expectations, prepare_calculators
        # WHEN/КОГДА
        prepare_calculators[name].__getattribute__(operation).__call__()
        captured = capsys.readouterr()
        # THEN/ТОГДА
        assert captured.out == expectations

    @pytest.fixture(scope='class')
    def prepare_to_test_advanced_operations(self, prepare_calculators):
        prepare_calculators['AdvCalc'].set_value(25, 2)
        return prepare_calculators

    @pytest.mark.parametrize(
        'operation,expectations',
        [
            pytest.param('power', "25 ** 2 = 625\n", id="25 ** 2 in AdvCalc"),
            pytest.param('square_root', "2√25 = 5.0\n", id="square_root25 in AdvCalc"),
        ]
    )
    def test_advanced_operations(self, operation, expectations, prepare_to_test_advanced_operations, capsys):
        """ Проверим выполнение продвинутых операций в AdvCalc """
        # GIVEN/ДАНО operation, expectations, prepare_calculators
        # WHEN/КОГДА
        prepare_to_test_advanced_operations['AdvCalc'].__getattribute__(operation).__call__()
        captured = capsys.readouterr()
        # THEN/ТОГДА
        assert captured.out == expectations
