from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()
def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()
def multiplicar():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()
    
def borrar():
    n1.set("")
    n2.set("")

#Configuración de la raíz
root = Tk()
root.config(bd=15)


n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify='center', textvariable=n1).pack() #primer numero
Label(root, text="Número 2").pack()
Entry(root, justify='center', textvariable=n2).pack() #segundo numero
Label(root, text="\nResultado").pack()
Entry(root, justify='center', textvariable=r, state='disabled').pack() #resultado
Label(root, text=" ").pack()
Button(root, text="Sumar", command=sumar).pack(side='left')
Button(root, text="Restar", command=restar).pack(side='left')
Button(root, text="Multiplicar", command=multiplicar).pack(side='left')



#Bucle de aplicación
root.mainloop()
