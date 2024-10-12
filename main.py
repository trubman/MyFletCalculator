import flet as ft
import referent

# CLI or FLET
MODE = 'CLI'

def main():
    pass

if __name__ == '__main__':
    if MODE == 'CLI':
        referent.get_input()
    elif MODE == 'FLET':
        ft.app(main)

