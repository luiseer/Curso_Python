from tkinter import *
from tkinter import messagebox as Messagebox


root = Tk()

def test():
    # Messagebox.showinfo("hola","Hola Mundo")
    # Messagebox.showwarning("Hola", "Hola Mundo")
    # Messagebox.showerror("hola", "Hola Mundo")
    # resultado = Messagebox.askquestion("Salir","Deseas salir sin guardar?")
    # if  resultado == "yes":
    #     root.destroy()
    # resultado = Messagebox.askokcancel("Salir","Deseas sobre escribir el fichero actual?")
    # resultado = Messagebox.askyesno("Salir","Deseas salir sin guardar?")
    # if resultado:
    #     root.destroy()
    resultado = Messagebox.askretrycancel("Reintentar", "No es posible establcer la conexión")
    if resultado:
        root.destroy()
        

Button(root, text="Click Aqui", command=test).pack()








root.mainloop()