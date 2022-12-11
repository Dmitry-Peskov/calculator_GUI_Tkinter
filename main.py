import tkinter as tk

def add_dijit(num: int):
    '''Добавляеn в поле ввода выбранную цифру'''
    value = calc.get() + str(num)
    calc.delete(0, tk.END)
    calc.insert(0, value)

#Настройки галвного окна
win = tk.Tk()
icon = tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.geometry(f"400x500+700+250")
win.title('Калькулятор (ПескOff production©)')
win.resizable(False, False)

#создаём поле ввода
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 20))
calc.grid(row=0, column=0, columnspan=3, sticky='we')

#настраиваем сетку
win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)
win.grid_columnconfigure(2,minsize=100)
win.grid_rowconfigure(1,minsize=100)
win.grid_rowconfigure(2,minsize=100)
win.grid_rowconfigure(3,minsize=100)
win.grid_rowconfigure(4,minsize=100)


tk.Button(text='7', font=('Arial',20), bd=2,command= lambda : add_dijit(7)).grid(row=1,column=0, sticky='wens', padx= 1, pady=1)
tk.Button(text='8', font=('Arial',20), bd=2,command= lambda : add_dijit(8)).grid(row=1,column=1, sticky='wens', padx= 1, pady=1)
tk.Button(text='9', font=('Arial',20), bd=2,command= lambda : add_dijit(9)).grid(row=1,column=2, sticky='wens', padx= 1, pady=1)
tk.Button(text='4', font=('Arial',20), bd=2,command= lambda : add_dijit(4)).grid(row=2,column=0, sticky='wens', padx= 1, pady=1)
tk.Button(text='5', font=('Arial',20), bd=2,command= lambda : add_dijit(5)).grid(row=2,column=1, sticky='wens', padx= 1, pady=1)
tk.Button(text='6', font=('Arial',20), bd=2,command= lambda : add_dijit(6)).grid(row=2,column=2, sticky='wens', padx= 1, pady=1)
tk.Button(text='1', font=('Arial',20), bd=2,command= lambda : add_dijit(1)).grid(row=3,column=0, sticky='wens', padx= 1, pady=1)
tk.Button(text='2', font=('Arial',20), bd=2,command= lambda : add_dijit(2)).grid(row=3,column=1, sticky='wens', padx= 1, pady=1)
tk.Button(text='3', font=('Arial',20), bd=2,command= lambda : add_dijit(3)).grid(row=3,column=2, sticky='wens', padx= 1, pady=1)
tk.Button(text='0', font=('Arial',20), bd=2,command= lambda : add_dijit(0)).grid(row=4,column=1, sticky='wens', padx= 1, pady=1)


if __name__ == "__main__":
    win.mainloop()