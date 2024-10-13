import flet as ft
from executor import Executor
from flet_gui import CalculatorApp
from tkinter_gui import tkinter_calc_gui

# CLI or FLET or TKI
MODE = 'TKI'

def main(page: ft.Page):
    page.title = "Неправильный калькулятор"
    page.window.width = 400
    page.window.height = 660
    page.window.resizable = False
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
    elif MODE == 'TKI':
        tkinter_calc_gui()

