import flet as ft

from executor import Executor


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text


class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK


class CalculatorApp(ft.Container):

    def __init__(self):
        super().__init__()
        # self.reset()

        self.width = 350
        self.padding = 20
        self.bgcolor = ft.colors.BLACK
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(20)

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.img = ft.Image(
            src="icon.jpg",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        )

        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.img], alignment="center"),
                ft.Row(controls=[ActionButton(text='=', button_clicked=self.go_math)]),
                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(controls=[
                    DigitButton(text="1", button_clicked=self.button_clicked),
                    DigitButton(text="2", button_clicked=self.button_clicked),
                    DigitButton(text="3", button_clicked=self.button_clicked),
                    DigitButton(text="4", button_clicked=self.button_clicked),
                    DigitButton(text="5", button_clicked=self.button_clicked),
                ]),
                ft.Row(controls=[
                    DigitButton(text="6", button_clicked=self.button_clicked),
                    DigitButton(text="7", button_clicked=self.button_clicked),
                    DigitButton(text="8", button_clicked=self.button_clicked),
                    DigitButton(text="9", button_clicked=self.button_clicked),
                    DigitButton(text="0", button_clicked=self.button_clicked),
                ]),
                ft.Row(controls=[
                    ActionButton(text="+", button_clicked=self.button_clicked),
                    ActionButton(text="-", button_clicked=self.button_clicked),
                    ActionButton(text="*", button_clicked=self.button_clicked),
                    ActionButton(text="/", button_clicked=self.button_clicked),
                ]),
                ft.Row(controls=[
                    ActionButton(text="**", button_clicked=self.button_clicked),
                    ActionButton(text="sqr", button_clicked=self.button_clicked),
                    DigitButton(text="чисто", button_clicked=self.reset),
                ]),
            ]
        )


    def button_clicked(self, e):
        button_dict = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "0": "0",
            "+": " + ",
            "-": " - ",
            "*": " * ",
            "/": " / ",
            "**": " ** ",
            "sqr": " sqr ",
        }
        data = e.control.data
        if self.result.value == '0':
            self.result.value = ''
            self.update()
        self.result.value += button_dict[data]
        self.update()

    def reset(self, e):
        if self.result.value != '0':
            self.result.value = '0'
            self.update()

    def go_math(self, e):
        exe = Executor()
        exe.cleaned_incoming = self.result.value.strip()
        exe.set_splited_values()
        result = exe.do_math()
        self.result.value = str(result)
        self.update()

