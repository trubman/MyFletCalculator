

class Calculator:

    def __init__(self):
        self._num1 = 0
        self._num2 = 0

    def set_value(self, num1, num2):
        try:
            self._num1 = int(num1)
            self._num2 = int(num2)
        except ValueError:
            print("Допустимы только целые числа!")

    def get_value(self):
        print(f'Текущия значения: {self._num1} и {self._num2}')

    def add(self):
        result = self._num1 + self._num2
        print(f'{self._num1} + {self._num2} = {result}')
        return result

    def substract(self):
        result = self._num1 - self._num2
        print(f'{self._num1} - {self._num2} = {result}')
        return result

    def multiply(self):
        result = self._num1 * self._num2
        print(f'{self._num1} * {self._num2} = {result}')
        return result

    def divide(self):
        try:
            result = self._num1 / self._num2
            print(f'{self._num1} / {self._num2} = {result:.2f}')
            return result
        except ZeroDivisionError:
            print("На ноль делить нельзя! (Во всяком случае в этом калькуляторе)")


class AdvancedCalculator(Calculator):

    def power(self):
        result = self._num1 ** self._num2
        print(f'{self._num1} ** {self._num2} = {result}')
        return result

    def square_root(self):
        try:
            if self._num1 >= 0:
                result = self._num1 ** (1/self._num2)
                print(f'{self._num2}√{self._num1} = {result}')
                return result
            else:
                raise ValueError
        except ValueError:
            print("Брать корень из отрицательного числа мы Вам не позволим!")

