from tkinter import *

root = Tk()


texto = Text(root)
texto.pack()
texto.config(
    width=100,
    height=100,
    font=('Cascadia Code', 13),
    padx=5,
    pady=5
)



root.mainloop()