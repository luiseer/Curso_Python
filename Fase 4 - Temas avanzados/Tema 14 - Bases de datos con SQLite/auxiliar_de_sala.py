import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import pandas as pd

def crear_tabla():
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS personas
                 (id INTEGER PRIMARY KEY,
                 nombre TEXT,
                 direccion TEXT,
                 telefono TEXT,
                 cedula_profesional TEXT)''')
    conn.commit()
    conn.close()

def agregar_persona():
    nombre = nombre_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()
    cedula_profesional = cedula_entry.get()

    if nombre.strip() == '' or direccion.strip() == '' or telefono.strip() == '' or cedula_profesional.strip() == '':
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    conn = sqlite3.connect('personas.db')
    c = conn.cursor()
    c.execute("INSERT INTO personas (nombre, direccion, telefono, cedula_profesional) VALUES (?, ?, ?, ?)",
              (nombre, direccion, telefono, cedula_profesional))
    conn.commit()
    conn.close()
    messagebox.showinfo("Éxito", "Persona agregada correctamente.")
    limpiar_campos()

def limpiar_campos():
    nombre_entry.delete(0, tk.END)
    direccion_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)
    cedula_entry.delete(0, tk.END)

def exportar_a_excel():
    conn = sqlite3.connect('personas.db')
    df = pd.read_sql_query("SELECT * FROM personas", conn)
    conn.close()

    filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if filename:
        df.to_excel(filename, index=False)
        messagebox.showinfo("Éxito", "Datos exportados correctamente a " + filename)

def main():
    crear_tabla()

    root = tk.Tk()
    root.title("Gestión de Personas")

    # Labels
    tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="e")
    tk.Label(root, text="Dirección:").grid(row=1, column=0, sticky="e")
    tk.Label(root, text="Teléfono:").grid(row=2, column=0, sticky="e")
    tk.Label(root, text="Cédula Profesional:").grid(row=3, column=0, sticky="e")

    # Entries
    global nombre_entry, direccion_entry, telefono_entry, cedula_entry
    nombre_entry = tk.Entry(root)
    direccion_entry = tk.Entry(root)
    telefono_entry = tk.Entry(root)
    cedula_entry = tk.Entry(root)
    nombre_entry.grid(row=0, column=1)
    direccion_entry.grid(row=1, column=1)
    telefono_entry.grid(row=2, column=1)
    cedula_entry.grid(row=3, column=1)

    # Buttons
    agregar_btn = tk.Button(root, text="Agregar Persona", command=agregar_persona)
    agregar_btn.grid(row=4, column=0, columnspan=2, pady=10)

    exportar_btn = tk.Button(root, text="Exportar a Excel", command=exportar_a_excel)
    exportar_btn.grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
