import flet as ft
from executor import Executor


# CLI or FLET
MODE = 'CLI'

def main():
    pass

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

