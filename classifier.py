from referent import Referent


class Classifier:

    def do_clean_input(self, incoming):
        if isinstance(incoming, str):
            return incoming.strip().lower()
        else:
            Referent.do_output(f"{incoming} - не является строкой")
            return False

    def check_input(self, cleaned_incoming):

        symbol_check = True
        for i in cleaned_incoming:
            if i not in "0123456789 +-*/**sqr":
                symbol_check = False

        splited_incoming = cleaned_incoming.split(" ")

        operation_check = True
        operations = ['+', '-', '*', '/', '**', 'sqr']
        for i in range(len(splited_incoming)):
            try:
                splited_incoming[i] = int(splited_incoming[i])
            except ValueError:
                if splited_incoming[i] not in operations:
                    operation_check = False

        if symbol_check and operation_check:
            return splited_incoming
        else:
            Referent.do_output(f"Выражение {cleaned_incoming} - недопустимо")
            return False





