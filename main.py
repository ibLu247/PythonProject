from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import random

fontPar = ("Arial", 16)

# Создание окна
window = Tk()
window.geometry("400x600")
window.resizable(True, True)
window.title("Оконное приложение")

# Создание вкладок
notebook = ttk.Notebook()
notebook.pack(expand = True, fill = BOTH)

# Функции
def enterName():
    value = entry1.get()
    showinfo(title = "Приветствие", message = f"Привет, {value}!")

def calculate():
    value = entry2.get()
    list = value.split()
    num1 = int(list[0])
    num2 = int(list[1])
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = "На ноль делить нельзя!"
    try:
        div = num1 / num2
    except:
        showerror(message = "Деление на ноль")
    showinfo(title = "Калькулятор", message = f" Сумма: {sum}\n Разность: {sub}\n Произведение: {mul}\n Частное: {div}")

def createList():
    list = []
    for i in range(10):
        list.append(int(random.random() * 50))

    originalList = list.copy()

    list.sort()

    # Сумма чисел в списке
    sum = 0
    for i in range(10):
        sum += list[i]

    showinfo(title = "Список", message = f" Список: {originalList}\n Отсортированный список: {list}\n Мин. значение: {max(list)}\n Макс. значение: {min(list)}\n Сумму чисел: {sum}")

def createFiles():
    number = 0
    for i in range(5):
        file_name = "file" + str(i + 1) + ".txt"
        file = open(file_name, "w")
        for i in range(10):
            n = (int(random.random() * 50))
            file.write(str(n) + " ")
        file.close()

    showinfo(title = "Успех!", message = "5 файлов успещно созданы")

def chooseAndReadFile():
    value = entry42.get()
    file = open("file" + str(value) + ".txt")
    fileContentString = file.read()
    fileContentNumber = [int(i) for i in fileContentString.split()]
    showinfo(title = f"{value}-й файл", message = f" Содержимое файла: {fileContentString}\n Среднее арифметическое: {sum(fileContentNumber) / len(fileContentNumber)}")


# Лаба №1
frame1 = ttk.Frame(padding = [0, 200])
frame1.pack()

label1 = ttk.Label(frame1, text = "Введите имя", font = fontPar)
label1.pack()

entry1 = ttk.Entry(frame1, font = fontPar)   
entry1.pack()

btn1 = ttk.Button(frame1, text = "Ввод", command = enterName)
btn1.pack()

# Лаба №2
frame2 = ttk.Frame(padding = [0, 200])
frame2.pack()

label2 = ttk.Label(frame2, text = "Введите два числа через пробел", font = fontPar)
label2.pack()

entry2 = ttk.Entry(frame2, font = fontPar)   
entry2.pack()

btn2 = ttk.Button(frame2, text = "Ввод", command = calculate)
btn2.pack()

# Лаба №3
frame3 = ttk.Frame(padding = [0, 200])
frame3.pack()

label3 = ttk.Label(frame3, text = "Создать список", font = fontPar)
label3.pack()

btn3 = ttk.Button(frame3, text = "Создать", command = createList)
btn3.pack()

# Лаба №4
frame4 = ttk.Frame(padding = [0, 200])
frame4.pack()

label41 = ttk.Label(frame4, text = "Создать файлы", font = fontPar)
label41.pack()

btn41 = ttk.Button(frame4, text = "Создать", command = createFiles)
btn41.pack()

label42 = ttk.Label(frame4, text = "Выберите файл (порядковый номер)", font = fontPar)
label42.pack()

entry42 = ttk.Entry(frame4, font = fontPar)   
entry42.pack()

btn42 = ttk.Button(frame4, text = "Выбрать", command =  chooseAndReadFile)
btn42.pack()

notebook.add(frame1, text="Вывод имени")
notebook.add(frame2, text="Калькулятор")
notebook.add(frame3, text="Список")
notebook.add(frame4, text="Файлы")

window.mainloop()