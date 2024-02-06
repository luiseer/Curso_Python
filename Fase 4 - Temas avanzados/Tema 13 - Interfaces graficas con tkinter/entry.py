from tkinter import *

#Configuración Raíz
root = Tk()

# frame = Frame(root)
# frame.pack()

label = Label(root, text='Nombre muy largo:')
label.grid(
    row=0, 
    column=0, 
    sticky='w',
    padx=5,
    pady=5
)
entry = Entry(root)
entry.grid(
    row=0, 
    column=1,
    padx=5,
    pady=5
)
entry.config(
    justify='right',
)

label1 = Label(root, text='Contraseña:')
label1.grid(
    row=1, 
    column=0, 
    sticky='w',
    padx=5,
    pady=5
)

entry1 = Entry(
    justify='center',
    show='*'
)
entry1.grid(row=1, column=1)



# frame1 = Frame(root)
# frame1.pack()



#Bucle de la alpicación
root.mainloop()