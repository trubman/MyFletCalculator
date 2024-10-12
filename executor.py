from calc import Calculator
from classifier import Classifier
from referent import Referent


class Executor:

    def __init__(self):
        self.cleaned_incoming = ""
        self.result = None
        self.splited_incoming = []
        self.classifier = Classifier()
        self.calculator = Calculator()

    def get_outgoing(self):
        if self.result:
            Referent.get_expression_result(self.cleaned_incoming, self.result)

    def set_cleaned_values(self, first=True):
        if first:
            incoming = Referent.get_mathematical_expression()
        else:
            incoming = Referent.get_input()

        def try_cleaned_incoming(incoming):
            cleaned_incoming = self.classifier.do_clean_input(incoming)
            if cleaned_incoming:
                self.cleaned_incoming = cleaned_incoming
            else:
                try_cleaned_incoming(Referent.get_input())

        try_cleaned_incoming(incoming)
        return self.cleaned_incoming

    def set_splited_values(self):
        splited_incoming = self.classifier.check_input(self.cleaned_incoming)

        if splited_incoming:
            self.splited_incoming = splited_incoming
        else:
            self.set_cleaned_values()

    def do_math(self):
        medium_result = None
        operation = None
        num2 = None
        count = 0
        for i in range(len(self.splited_incoming)):

            if isinstance(self.splited_incoming[i], int):
                if medium_result == None:
                    medium_result = self.splited_incoming[i]
                else:
                    num2 = self.splited_incoming[i]
            else:
                operation = self.splited_incoming[i]
            count += 1

            if count == 3:
                result = self.calculator.__getattribute__(operation).__call__(medium_result, num2)
                count = 1
                if result:
                    medium_result = result
                    self.result = medium_result
                    return medium_result
                else:
                    Referent.do_output("¯\_(ツ)_/¯ - мои полномочия все...")
                    return False

