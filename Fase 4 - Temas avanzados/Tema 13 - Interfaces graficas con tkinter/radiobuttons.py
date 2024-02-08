from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(option.get()))

def reset():
    option.set(None)
    monitor.config(text=" ")

root = Tk()

option = IntVar()

Radiobutton(root, text='Opcion 1', variable=option, value=1, command=seleccionar).pack()
Radiobutton(root, text='Opcion 2', variable=option, value=2, command=seleccionar).pack()
Radiobutton(root, text='Opcion 3', variable=option, value=3, command=seleccionar).pack()

monitor = Label(root,)
monitor.pack()

Button(root, text="reiniciar", command=reset).pack()

root.mainloop()