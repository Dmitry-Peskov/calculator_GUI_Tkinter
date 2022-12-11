import tkinter as tk

def add_dijit(num: str):
    '''Добавляет в поле ввода выбранную цифру'''
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + num)
    
def add_operation(operation: str):
    '''Добавляет операцию в поле ввода'''
    value = calc.get() 
    if value[-1] in '-+*/':
        value = value[:-1] 
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():
    '''Производит вычеснение на основе выражения записанного в строке ввода'''
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))

def clear():
    '''Очищает поле ввода'''
    calc.delete(0, tk.END)
    calc.insert(0,0)

def create_button_dijit(num: int):
    '''Создаёт кнопку'''
    return tk.Button(text= str(num), font=('Arial',20), bd=2,command= lambda : add_dijit(num))

def create_button_operation(operation: str):
    '''Создаёт кнопки математических операций'''
    return tk.Button(text= str(operation), font=('Impact',20), bd=2,command= lambda : add_operation(operation))

def create_button_calc(operation: str):
    '''Создаёт кнопку равенства'''
    return tk.Button(text= str(operation), font=('Impact',20), bd=2,command= calculate)

def create_button_clear(operation: str):
    '''Создаёт кнопку равенства'''
    return tk.Button(text= str(operation), font=('Impact',20), bd=2,command= clear)

#Настройки галвного окна
win = tk.Tk()
icon = tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.geometry(f"400x500+700+250")
win.title('Калькулятор (ПескOff production©)')
win.resizable(False, False)

#создаём поле ввода
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 20))
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx= 10)
calc.insert(0,'0')

#настраиваем сетку
win.grid_columnconfigure(0,minsize=90)
win.grid_columnconfigure(1,minsize=90)
win.grid_columnconfigure(2,minsize=90)
win.grid_columnconfigure(3,minsize=90)
win.grid_rowconfigure(1,minsize=90)
win.grid_rowconfigure(2,minsize=90)
win.grid_rowconfigure(3,minsize=90)
win.grid_rowconfigure(4,minsize=90)

#создаём кнопки с цифрами
create_button_dijit('7').grid(row=1,column=0, sticky='wens', padx= 1, pady=1)
create_button_dijit('8').grid(row=1,column=1, sticky='wens', padx= 1, pady=1)
create_button_dijit('9').grid(row=1,column=2, sticky='wens', padx= 1, pady=1)
create_button_dijit('4').grid(row=2,column=0, sticky='wens', padx= 1, pady=1)
create_button_dijit('5').grid(row=2,column=1, sticky='wens', padx= 1, pady=1)
create_button_dijit('6').grid(row=2,column=2, sticky='wens', padx= 1, pady=1)
create_button_dijit('1').grid(row=3,column=0, sticky='wens', padx= 1, pady=1)
create_button_dijit('2').grid(row=3,column=1, sticky='wens', padx= 1, pady=1)
create_button_dijit('3').grid(row=3,column=2, sticky='wens', padx= 1, pady=1)
create_button_dijit('0').grid(row=4,column=1, sticky='wens', padx= 1, pady=1)

#создаём кнопки с математическими операциями
create_button_operation('/').grid(row=1,column=3, sticky='wens', padx= 1, pady=1)
create_button_operation('*').grid(row=2,column=3, sticky='wens', padx= 1, pady=1)
create_button_operation('-').grid(row=3,column=3, sticky='wens', padx= 1, pady=1)
create_button_operation('+').grid(row=4,column=3, sticky='wens', padx= 1, pady=1)

#создаем кнопки вычисления и очистки
create_button_calc('=').grid(row=4,column=2, sticky='wens', padx= 1, pady=1)
create_button_clear('C').grid(row=4,column=0, sticky='wens', padx= 1, pady=1)

if __name__ == "__main__":
    win.mainloop()