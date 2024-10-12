from referent import Referent


class Classifier:

    def do_clean_input(self, incoming):
        if isinstance(incoming, str):
            return incoming.strip().lower()
        else:
            Referent.do_output(f"{incoming} - не является строкой")


