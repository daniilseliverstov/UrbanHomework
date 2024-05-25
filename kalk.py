import tkinter as tk
def get_values():
    numb1 = int(number1_entry.get())
    numb2 = int(number2_entry.get())
    return numb1, numb2
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    numb1, numb2 = get_values()
    res = numb1 + numb2
    insert_values(res)

def sub():
    numb1, numb2 = get_values()
    res = numb1 - numb2
    insert_values(res)

def div():
    numb1, numb2 = get_values()
    res = numb1 / numb2
    insert_values(res)

def mul():
    numb1, numb2 = get_values()
    res = numb1 * numb2
    insert_values(res)










window = tk.Tk()
window.title('Калькулятор')
window.geometry("300x300")
window.resizable(False,False)
button_add = tk.Button(window, text = '+', width=2, height=1, command=add)
button_add.place(x = 50, y = 150)
button_sub = tk.Button(window, text = '-', width=2, height=1, command=sub)
button_sub.place(x = 100, y = 150)
button_mul = tk.Button(window, text = 'x', width=2, height=1, command=mul)
button_mul.place(x = 150, y = 150)
button_div = tk.Button(window, text = '/', width=2, height=1, command=div)
button_div.place(x = 200, y = 150)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x = 50, y = 50)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x = 50, y = 100)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x = 50, y = 200)
number1 = tk.Label(window, text='Введите первое число')
number1.place(x = 50, y = 70)
number2 = tk.Label(window, text='Введите второе число')
number2.place(x = 50, y = 120)
answer = tk.Label(window, text='Ответ')
answer.place(x = 50, y = 220)
window.mainloop()