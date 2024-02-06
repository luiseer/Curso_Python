from tkinter import *
root = Tk()

root.title("hola mundo")
root.iconbitmap('hola.ico')

frame = Frame(root, width=400, height=380)

frame.pack(fill='both', expand='1')

frame.config(cursor="pirate")
frame.config(bg='lightblue')
frame.config(bd=25)
frame.config(relief='sunken')


root.config(cursor="pirate")
root.config(bg='blue')
root.config(bd=35)
root.config(relief='ridge')




root.mainloop()
