import functions
from random import randint
from tkinter import *
from tkinter import font
from tkinter import END, INSERT, messagebox as mb
import os
import sys

root = Tk()
root.title("Крестики нолики")
root.geometry("290x300+400+400")
root.resizable(width = False, height = False)
o = str('o')
x = str('x')

l1 = Label(root, text='Для выполнения хода, введите\n"О" в свободную ячейку и нажмте Enter', font=("Arial", 11))
l1.place(x = 10, y = 210)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
v9 = StringVar()

e1 = Entry(root, textvariable = v1, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e1.place(x = 50, y = 10)
e2 = Entry(root, textvariable = v2, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e2.place(x = 110, y = 10)
e3 = Entry(root, textvariable = v3, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e3.place(x = 170, y = 10)
e4 = Entry(root, textvariable = v4, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e4.place(x = 50, y = 55)
e5 = Entry(root, textvariable = v5, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e5.place(x = 110, y = 55)
e6 = Entry(root, textvariable = v6, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e6.place(x = 170, y = 55)
e7 = Entry(root, textvariable = v7, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e7.place(x = 50, y = 100)
e8 = Entry(root, textvariable = v8, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e8.place(x = 110, y = 100)
e9 = Entry(root, textvariable = v9, width = 3, justify = CENTER,
        font=font.Font(family="Arial Black", size = 21))
e9.place(x = 170, y = 100)


def for_enter():  # основная программа
        functions.winner() 
        functions.add_x_after_xx()
        functions.winner() 
        functions.add_x_after_oo()
        functions.winner() 
        functions.add_x()        
        functions.winner()    

def check_mistake(_a, _e): # выводит сообщение об ошибке при введении значения отличного от "О"
        if _a != o:
                mb.showerror("Ошибка", "Должно быть введено 'o'")
                _e.delete(0, END)
                button_click()
        else: for_enter() # переходит к основной программе

def enter1(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e1
        a1 = v1.get()
        check_mistake(a1, e1)
def enter2(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e2
        a2 = v2.get()
        check_mistake(a2, e2)
def enter3(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e3
        a3 = v3.get()
        check_mistake(a3, e3)
def enter4(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e4
        a4 = v4.get()
        check_mistake(a4, e4)
def enter5(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e5
        a5 = v5.get()
        check_mistake(a5, e5)
def enter6(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e6
        a6 = v6.get()
        check_mistake(a6, e6)
def enter7(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e7
        a7 = v7.get()
        check_mistake(a7, e7)
def enter8(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e8
        a8 = v8.get()
        check_mistake(a8, e8)
def enter9(event): # обрабатывает нажатие клавиши Enter после ввода данных в поле e9
        a9 = v9.get()
        check_mistake(a9, e9)


e1.bind('<Return>', enter1) # при нажатии кнопки Enter на клавиатуре вызывается функция enter1
e2.bind('<Return>', enter2)
e3.bind('<Return>', enter3)
e4.bind('<Return>', enter4)
e5.bind('<Return>', enter5)
e6.bind('<Return>', enter6)
e7.bind('<Return>', enter7)
e8.bind('<Return>', enter8)
e9.bind('<Return>', enter9)

rand = randint(0, 1)    # случайным образом выбирается кто делает первый ход
if rand == 0:
        l2 = Label(root, text = "Первый ход сделал бот", font=("Arial", 10))
        l2.place(x = 60, y = 160)
        functions.bot_first_move()
if rand == 1:
        l3 = Label(root, text = "Вы ходите первым", font=("Arial", 10))
        l3.place(x = 75, y = 180)

def button_click():
        print()

root.mainloop()

