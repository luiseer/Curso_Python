from tkinter import *
from tkinter import filedialog as Filedialog
from io import open


ruta = "" #la usamos para saber si existe la ruta de un fichero

def new():
    global ruta
    mensaje.set("Este es un fichero Nuevo  :-)")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("My Editor")
    
def open_file():
    global ruta
    mensaje.set("Este es un fichero abierto  B-)")
    ruta = Filedialog.askopenfilename(  
        initialdir='.',
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un archivo de texto"
    )
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " -My Editor")
        
        
def save():
    mensaje.set("Guardar Fichero :-)")
    if ruta != "":
        contenido = texto.get(1.0, "end-c")
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente :p")
    else:
        save_as()
        
        
def save_as():
    global ruta
    mensaje.set("Guardar como Fichero :-)")
    fichero = Filedialog.asksaveasfile(
        title="Guardar fichero",
        mode="w",
        defaultextension=".txt"
    )
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-c")
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente :p")
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""

root = Tk()
root.title("Text Editor")


#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(menu=filemenu, label="File")

#Caje de texto Central
texto = Text(root)
texto.pack(
    fill="both", 
    expand=1)
texto.config(
    bd=0,
    padx=6,
    pady=4,
    font=('Cascadia Code', 13))

#Monitor inferior
mensaje = StringVar()
mensaje.set("Bien Benivo al Editor :)")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack()




root.config(menu=menubar)
root.mainloop()