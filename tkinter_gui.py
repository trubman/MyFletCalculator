from tkinter import *
from PIL import ImageTk, Image

from executor import Executor


def tkinter_calc_gui():
    root = Tk()
    root.title('Неправильный калькулятор')

    def button_add(text):
        e.config(state=NORMAL)
        if e.get() == "0":
            e.delete(0, END)
        e.insert(END, text)
        e.config(state=DISABLED)

    def button_clear():
        e.config(state=NORMAL)
        e.delete(0, END)
        e.insert(END, '0')
        e.config(state=DISABLED)

    def button_equal():
        exe = Executor()
        exe.cleaned_incoming = e.get().strip()
        exe.set_splited_values()
        result = exe.do_math()
        if not result:
            result = 'Error'
        e.config(state=NORMAL)
        e.delete(0, END)
        e.insert(END, str(result))
        e.config(state=DISABLED)

    canv = Canvas(root, width=300, height=300, bg='white')
    canv.grid(row=0, column=0, columnspan=3)
    i = Image.open("icon.jpg")
    i2 = i.resize((300, 300))
    img = ImageTk.PhotoImage(i2)
    canv.create_image(0, 0, anchor=NW, image=img)

    button_equal = Button(root, text='=', padx=130, pady=10, command=button_equal)
    button_equal.grid(row=1, column=0, columnspan=3)

    e = Entry(root, width=40, borderwidth=5)
    e.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    e.insert(END, '0')
    e.config(state=DISABLED)


    button_1 = Button(root, text='1', padx=40, pady=10, command=lambda:button_add("1"))
    button_2 = Button(root, text='2', padx=40, pady=10, command=lambda:button_add("2"))
    button_3 = Button(root, text='3', padx=40, pady=10, command=lambda:button_add("3"))
    button_4 = Button(root, text='4', padx=40, pady=10, command=lambda:button_add("4"))
    button_5 = Button(root, text='5', padx=40, pady=10, command=lambda:button_add("5"))
    button_6 = Button(root, text='6', padx=40, pady=10, command=lambda:button_add("6"))
    button_7 = Button(root, text='7', padx=40, pady=10, command=lambda:button_add("7"))
    button_8 = Button(root, text='8', padx=40, pady=10, command=lambda:button_add("8"))
    button_9 = Button(root, text='9', padx=40, pady=10, command=lambda:button_add("9"))
    button_0 = Button(root, text='0', padx=40, pady=10, command=lambda:button_add("0"))
    button_clear = Button(root, text='чисто', padx=78, pady=10, command=button_clear)

    button_add_b = Button(root, text='+', padx=40, pady=10, command=lambda:button_add(" + "))
    button_substract = Button(root, text='-', padx=40, pady=10, command=lambda:button_add(" - "))
    button_multiply = Button(root, text='*', padx=40, pady=10, command=lambda:button_add(" * "))
    button_divide = Button(root, text='/', padx=40, pady=10, command=lambda:button_add(" / "))
    button_power = Button(root, text='**', padx=38, pady=10, command=lambda:button_add(" ** "))
    button_square_root = Button(root, text='sqr', padx=34, pady=10, command=lambda:button_add(" sqr "))

    button_0.grid(row=3, column=0)
    button_clear.grid(row=3, column=1, columnspan=2)

    button_1.grid(row=6, column=0)
    button_2.grid(row=6, column=1)
    button_3.grid(row=6, column=2)

    button_4.grid(row=5, column=0)
    button_5.grid(row=5, column=1)
    button_6.grid(row=5, column=2)

    button_7.grid(row=4, column=0)
    button_8.grid(row=4, column=1)
    button_9.grid(row=4, column=2)

    button_add_b.grid(row=7, column=0)
    button_substract.grid(row=7, column=1)
    button_multiply.grid(row=7, column=2)

    button_divide.grid(row=8, column=0)
    button_power.grid(row=8, column=1)
    button_square_root.grid(row=8, column=2)

    root.mainloop()