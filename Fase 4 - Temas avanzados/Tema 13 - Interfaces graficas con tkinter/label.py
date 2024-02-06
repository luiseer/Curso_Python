from tkinter import *

#Configurción de la raíz
root = Tk()

"""
#Strings bars o variables dinamicas
texto = StringVar()
texto.set('Un nuevo Texto')
#configuración de un marco
#frame = Frame( root, width=480, height='320')
#frame.pack()

#Etiquetas
Label(root, text='hoal mundo').pack(anchor='nw')
label = Label(root, text='Otra Etiqueta')
label.pack(anchor='center')
Label(root, text='Ultima etiqueta!').pack(anchor='se')

label.config(
            bg='green', 
            fg='blue',
            font=('Cascadia Code', 22)
                )
label.config(textvariable=texto)

"""
imagen = PhotoImage(file='imagen.gif')
Label(root, image=imagen, bd=0).pack(side='top')




#Bucle del programa
root.mainloop()
