import flet as ft
from executor import Executor
from flet_gui import CalculatorApp


# CLI or FLET
MODE = 'FLET'

def main():
    page = ft.Page()
    page.title = "Неправильный калькулятор"

    calc = CalculatorApp()

    page.add(calc)

if __name__ == '__main__':
    if MODE == 'CLI':
        first = True
        while True:
            ex = Executor()
            incoming = ex.set_cleaned_values(first)
            if incoming == 'break':
                break
            ex.set_splited_values()
            ex.do_math()
            ex.get_outgoing()
            first = False
    elif MODE == 'FLET':
        ft.app(main)

