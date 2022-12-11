import tkinter as tk

#Настройки галвного окна
win = tk.Tk()
icon = tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.geometry(f"400x500+700+250")
win.title('Калькулятор (ПескOff production©)')
win.resizable(False, False)


if __name__ == "__main__":
    win.mainloop()