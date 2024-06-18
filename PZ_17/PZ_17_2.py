# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ№ 2-9 (я взял 2)

import tkinter as tk


def calculate_cost(x, a, y, b):
    try:
        if x == "" or a == "" or y == "" or b == "":
            return "введите все значения!", "", ""

        x = abs(float(x))
        a = abs(float(a))
        y = abs(float(y))
        b = abs(float(b))

        s1 = round(a / x, 5)
        s2 = round(b / y, 5)
        s3 = round(s1 / s2, 5)

        return ("стоимость 1 кг шоколадных конфет: " + str(s1),
                "стоимость 1 кг ирисок: " + str(s2),
                "шоколадные конфеты дороже ирисок в " + str(s3) + " раз")
    except ValueError:
        return "вводить надо числа!", "", ""
    except ZeroDivisionError:
        return "нельзя делить на ноль!", "", ""


def button_press(event):
    global t1, t2, t3
    c.delete(t1), c.delete(t2), c.delete(t3)
    c.tk.call("focus", window)
    x = xe.get()
    a = ae.get()
    y = ye.get()
    b = be.get()
    s1, s2, s3 = calculate_cost(x, a, y, b)
    t1 = c.create_text(20, 230, font=('Times New Roman', 13), text=s1, anchor=tk.W)
    t2 = c.create_text(20, 260, font=('Times New Roman', 13), text=s2, anchor=tk.W)
    t3 = c.create_text(20, 290, font=('Times New Roman', 13), text=s3, anchor=tk.W)


window = tk.Tk()
window.geometry("400x350")
window.resizable(False, False)
c = tk.Canvas(width=400, height=350, highlightthickness=0)
c.pack()

c.create_text(200, 20, font=('Times New Roman', 16), text="Введите данные")

t1 = c.create_text(20, 210, font=('Times New Roman', 14), text="", anchor=tk.W)
t2 = c.create_text(20, 240, font=('Times New Roman', 14), text="", anchor=tk.W)
t3 = c.create_text(20, 270, font=('Times New Roman', 14), text="", anchor=tk.W)

xe = tk.Entry(font=('Times New Roman', 14))
ae = tk.Entry(font=('Times New Roman', 14))
ye = tk.Entry(font=('Times New Roman', 14))
be = tk.Entry(font=('Times New Roman', 14))
xe.place(width=50, height=30, anchor=tk.NW, x=180, y=50)
ae.place(width=50, height=30, anchor=tk.NW, x=280, y=50)
ye.place(width=50, height=30, anchor=tk.NW, x=180, y=100)
be.place(width=50, height=30, anchor=tk.NW, x=280, y=100)

c.create_text(20, 65, font=('Times New Roman', 12), text="шоколадные конфеты", anchor=tk.W)
c.create_text(240, 65, font=('Times New Roman', 14), text="кг", anchor=tk.W)
c.create_text(340, 65, font=('Times New Roman', 14), text="цена", anchor=tk.W)
c.create_text(20, 115, font=('Times New Roman', 12), text="ириски", anchor=tk.W)
c.create_text(240, 115, font=('Times New Roman', 14), text="кг", anchor=tk.W)
c.create_text(340, 115, font=('Times New Roman', 14), text="цена", anchor=tk.W)

bu = tk.Button(font=('Times New Roman', 16), fg='white', bg='grey', text='расчитать', width=10)
bu.place(x=200, y=180, anchor=tk.CENTER)
bu.bind("<Button-1>", button_press)

window.mainloop()
