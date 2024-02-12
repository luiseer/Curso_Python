from tkinter import *

ruta = "" #la usamos para saber si existe la ruta de un fichero

def new():
    global ruta
    mensaje.set("Este es un fichero Nuevo :-)")
    ruta = ""
    texto.delete(1.0, "end")
def open():
    mensaje.set("Abrir fichero :-)")
def save():
    mensaje.set("Guardar Fichero :-)")
def save_as():
    mensaje.set("Guardar como Fichero :-)")


root = Tk()
root.title("Text Editor")


#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(menu=filemenu, label="File")

#Caje de texto Central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0,padx=6,pady=4,font=('Cascadia Code', 13))

#Monitor inferior
mensaje = StringVar()
mensaje.set("Bien Benivo al Editor :)")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack()




root.config(menu=menubar)
root.mainloop()