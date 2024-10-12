import flet as ft
from referent import Referent

# CLI or FLET
MODE = 'CLI'

def main():
    pass

if __name__ == '__main__':
    if MODE == 'CLI':
        Referent.get_expression_result(Referent.get_mathematical_expression(), 4)
    elif MODE == 'FLET':
        ft.app(main)

