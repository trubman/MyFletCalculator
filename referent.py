
class Referent:

    @staticmethod
    def get_input():
        incoming = input()
        return incoming

    @staticmethod
    def do_output(incoming):
        print(f"{incoming}")

    @staticmethod
    def get_mathematical_expression():
        Referent.do_output("Введите математическое выражение (через пробел):")
        Referent.do_output("(Доступные операции: +, -, *, /, **, sqr)")
        incoming = Referent.get_input()
        return incoming

    # @staticmethod
    # def get_expression_result(incoming, result):
    #     Referent.do_output(f"{incoming} = {result}")
