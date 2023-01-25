from tkinter import *
import controller

o = str('o')
x = str('x')
a1, a2, a3, a4, a5, a6, a7, a8, a9 = 0, 0, 0, 0, 0, 0, 0, 0, 0


def add_x_after_xx():   # дополняет два "х" "х" третьим "х" на одной линии
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, k
    k = int(0)      # k нужна для избегания повторяемости в одном цикле программы (добавления лишних крестиков)
    a1 = controller.v1.get()
    a2 = controller.v2.get()
    a3 = controller.v3.get()
    a4 = controller.v4.get()
    a5 = controller.v5.get()
    a6 = controller.v6.get()
    a7 = controller.v7.get()
    a8 = controller.v8.get()
    a9 = controller.v9.get()
    if a1 == x and a2 == x or a6 == x and a9 == x or a7 == x and a5 == x:
        if a3 != x and a3 != o and k != 1:
            controller.e3.insert(INSERT, "x")
            a3 = x
            k = 1
    if a1 == x and a4 == x or a9 == x and a8 == x or a3 == x and a5 == x:
        if a7 != x and a7 != o and k != 1:
            controller.e7.insert(INSERT, "x")
            a7 = x
            k = 1
    if a2 == x and a3 == x or a7 == x and a4 == x or a9 == x and a5 == x:
        if a1 != x and a1 != o and k != 1:
            controller.e1.insert(INSERT, "x")
            a1 = x
            k = 1
    if a3 == x and a6 == x or a7 == x and a8 == x or a1 == x and a5 == x:
        if a9 != x and a9 != o and k != 1:
            controller.e9.insert(INSERT, "x")
            a9 = x
            k = 1
    if a8 == x and a5 == x or a1 == x and a3 == x:
        if a2 != x and a2 != o and k != 1:
            controller.e2.insert(INSERT, "x")
            a2 = x
            k = 1
    if a2 == x and a5 == x or a7 == x and a9 == x:
        if a8 != x and a8 != o and k != 1:
            controller.e8.insert(INSERT, "x")
            a8 = x
            k = 1
    if a4 == x and a5 == x or a3 == x and a9 == x:
        if a6 != x and a6 != o and k != 1:
            controller.e6.insert(INSERT, "x")
            a6 = x
            k = 1
    if a5 == x and a6 == x or a1 == x and a7 == x:
        if a4 != x and a4 != o and k != 1:
            controller.e4.insert(INSERT, "x")
            a4 = x
            k = 1
    if a1 == x and a9 == x or a3 == x and a7 == x or a4 == x and a6 == x or a2 == x and a8 == x:
        if a5 != x and a5 != o and k != 1:
            controller.e5.insert(INSERT, "x")
            a5 = x
            k = 1

def add_x_after_oo():      # ставит 'x' перед двумя подряд "o", 'o'
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, l
    l = int(0)
    a1 = controller.v1.get()
    a2 = controller.v2.get()
    a3 = controller.v3.get()
    a4 = controller.v4.get()
    a5 = controller.v5.get()
    a6 = controller.v6.get()
    a7 = controller.v7.get()
    a8 = controller.v8.get()
    a9 = controller.v9.get()
    if a1 == o and a2 == o or a6 == o and a9 == o or a7 == o and a5 == o:
        if a3 != x and a3 != o and k != 1:
            controller.e3.insert(INSERT, "x") # бот ставит "Х" в поле е3
            a3 = x
            l = 1
    if a1 == o and a4 == o or a9 == o and a8 == o or a3 == o and a5 == o:
        if a7 != x and a7 != o and l != 1 and k != 1:
            controller.e7.insert(INSERT, "x") # бот ставит "Х" в поле е7
            a7 = x
            l = 1
    if a2 == o and a3 == o or a7 == o and a4 == o or a9 == o and a5 == o:
        if a1 != x and a1 != o and l != 1 and k != 1:
            controller.e1.insert(INSERT, "x")
            a1 = x
            l = 1
    if a3 == o and a6 == o or a7 == o and a8 == o or a1 == o and a5 == o:
        if a9 != x and a9 != o and l != 1 and k != 1:
            controller.e9.insert(INSERT, "x")
            a9 = x
            l = 1
    if a8 == o and a5 == o or a1 == o and a3 == o:
        if a2 != x and a2 != o and l != 1 and k != 1:
            controller.e2.insert(INSERT, "x")
            a2 = x
            l = 1
    if a2 == o and a5 == o or a7 == o and a9 == o:
        if a8 != x and a8 != o and l != 1 and k != 1:
            controller.e8.insert(INSERT, "x")
            a8 = x
            l = 1
    if a4 == o and a5 == o or a3 == o and a9 == o:
        if a6 != x and a6 != o and l != 1 and k != 1:
            controller.e6.insert(INSERT, "x")
            a6 = x
            l = 1
    if a5 == o and a6 == o or a1 == o and a7 == o:
        if a4 != x and a4 != o and l != 1 and k != 1:
            controller.e4.insert(INSERT, "x")
            a4 = x
            l = 1
    if a2 == o and a8 == o or a4 == o and a6 == o or a3 == o and a7 == o or a1 == o and a9 == o:
        if a5 != x and a5 != o and l != 1 and k != 1:
            controller.e5.insert(INSERT, "x")
            a5 = x
            l = 1

def add_x():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, n
    n = int(0) # n нужна для избегания повторяемости (добавления лишних крестиков)
    a1 = controller.v1.get()
    a2 = controller.v2.get()
    a3 = controller.v3.get()
    a4 = controller.v4.get()
    a5 = controller.v5.get()
    a6 = controller.v6.get()
    a7 = controller.v7.get()
    a8 = controller.v8.get()
    a9 = controller.v9.get()
    if  a1 != x and a1 != o and l != 1 and k != 1:
        controller.e1.insert(INSERT, "x") # бот вставляет "Х" в поле е1
        a1 = x
        n = int(1)
    elif  a2 != x and a2 != o and n != 1 and l != 1 and k != 1:
        controller.e2.insert(INSERT, "x")
        a2 = x
        n = int(1)
    elif  a3 != x and a3 != o and n != 1  and l != 1 and k != 1:
        controller.e3.insert(INSERT, "x")
        a3 = x
        n = int(1)
    elif  a4 != x and a4 != o and n != 1  and l != 1 and k != 1:
        controller.e4.insert(INSERT, "x")
        a4 = x
        n = int(1)
    elif  a5 != x and a5 != o and n != 1 and l != 1 and k != 1:
        controller.e5.insert(INSERT, "x")
        a5 = x
        n = int(1)
    elif  a6 != x and a6 != o and n != 1 and l != 1 and k != 1:
        controller.e6.insert(INSERT, "x")
        a6 = x
        n = int(1)
    elif  a7 != x and a7 != o and n != 1 and l != 1 and k != 1:
        controller.e7.insert(INSERT, "x")
        a7 = x
        n = int(1)
    elif  a8 != x and a8 != o and n != 1 and l != 1 and k != 1:
        controller.e8.insert(INSERT, "x")
        a8 = x
        n = int(1)
    elif  a9 != x and a9 != o and n != 1 and l != 1 and k != 1:
        controller.e9.insert(INSERT, "x")
        a9 = x
        n = int(1)

def bot_first_move():
    global a5
    if a5 != x:
        print("bot_firs_move")
        controller.e5.insert(INSERT, "x")
        a5 = x


def winner(): # проверяет выигрышные и ничейные ппозиции  и передает статус в контроллер
    global a1, a2, a3, a4, a5, a6, a7, a8, a9
    a1 = controller.v1.get()
    a2 = controller.v2.get()
    a3 = controller.v3.get()
    a4 = controller.v4.get()
    a5 = controller.v5.get()
    a6 = controller.v6.get()
    a7 = controller.v7.get()
    a8 = controller.v8.get()
    a9 = controller.v9.get()
    if (a1 == x and a2 == x and a3 == x) or (a4 == x and a5 == x and a6 == x) or (a7 == x and a8 == x and a9 == x) or (a1 == x and a4 == x and a7 == x) or (a2 == x and a5 == x and a8 == x) or (a3 == x and a6 == x and a9 == x) or (a1 == x and a5 == x and a9 == x) or (a7 == x and a5 == x and a3 == x):
        l4 = Tk() # вывод в отдельном окне результата игры
        l4.title("Результат игры")
        l4.geometry("290x25+400+700")
        label_aa = Label(l4, text = "Вы проиграли", font = ("Arial Black", 12), fg = "blue")
        label_aa.pack()
        l4.mainloop()
        quit()
    elif (a1 == o and a2 == o and a3 == o) or (a4 == o and a5 == o and a6 == o) or (a7 == o and a8 == o and a9 == o) or (a1 == o and a4 == o and a7 == o) or (a2 == o and a5 == o and a8 == o) or (a3 == o and a6 == o and a9 == o) or (a1 == o and a5 == o and a9 == o) or (a7 == o and a5 == o and a3 == o):
        l4 = Tk() # вывод в отдельном окне результата игры
        l4.title("Результат игры")
        l4.geometry("290x25+400+700")
        label_aa = Label(l4, text = "Вы выиграли", font = ("Arial Black", 12), fg = "blue")
        label_aa.pack()
        l4.mainloop()
        quit()
    elif (a1 == o or a1 == x) and (a2 == o or a2 == x) and (a3 == o or a3 == x) and (a4 == o or a4 == x) and (a5 == o or a5 == x) and (a6 == o or a6 == x) and (a7 == o or a7 == x) and (a8 == o or a8 == x) and (a9 == o or a9 == x):
        l4 = Tk() # вывод в отдельном окне результата игры
        l4.title("Результат игры")
        l4.geometry("290x25+400+700")
        label_aa = Label(l4, text = "Ничья", font = ("Arial Black", 12), fg = "blue")
        label_aa.pack()
        l4.mainloop()
        quit()


