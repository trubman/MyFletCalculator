from referent import Referent


class Calculator:

    def add(self, num1, num2):
        result = num1 + num2
        return result

    def substract(self, num1, num2):
        result = num1 - num2
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        return result

    def divide(self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            Referent.do_output("На ноль делить нельзя! (Во всяком случае в этом калькуляторе)")
            return False

    def power(self, num1, num2):
        result = num1 ** num2
        return result

    def square_root(self, num1, num2):
        try:
            if num1 >= 0:
                result = num1 ** (1/num2)
                return result
            else:
                raise ValueError
        except ValueError:
            Referent.do_output("Брать корень из отрицательного числа мы Вам не позволим!")
            return False

