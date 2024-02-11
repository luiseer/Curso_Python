from tkinter import *
from tkinter import messagebox as Messagebox
from tkinter import colorchooser as Colorchooser
from tkinter import filedialog as Filedialog

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
    # resultado = Messagebox.askretrycancel("Reintentar", "No es posible establcer la conexión")
    # if resultado:
    #     root.destroy()
    # color = Colorchooser.askcolor(title="Elije un color")
    # print(color)
    # ruta = Filedialog.askopenfile(
    #     title="Abrir un ruta", 
    #     initialdir="home", 
    #     filetypes=(("Ficheros PDF", "*.pdf"),
    #                ("Ficheros de texto", "*.txt"))
    #     )
    # print(ruta)
    fichero = Filedialog.asksaveasfile(title="Guardar un fichero", mode="r+", defaultextension=".txt") #Equivale a ruta y abrir el fichero en w
    if fichero is not None:
        fichero.write("hola!")
        fichero.close()
        
    
        
        

Button(root, text="Click Aqui", command=test).pack()








root.mainloop()