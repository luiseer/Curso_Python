import sqlite3

def create_db():
    conexion = sqlite3.connect("restaurante.bd")
    cursor = conexion.cursor()
    try:
        cursor.execute('''CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla ya existe")
    else:
        print("La tabla fue creada con éxito")
    try:
        cursor.execute('''CREATE TABLE plato(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) UNIQUE NOT NULL, 
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
        
    except sqlite3.OperationalError:
        print("La tabla ya existe")
    else:
        print("La tabla fue creada con éxito")
    
    conexion.close()

def crear_categoria():
    categoria = input("Nombre de la categoría nueva ?\n>")
    conexion = sqlite3.connect("restaurante.bd")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES(NULL, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya existe".format(categoria))
    else:
        print("Categoría '{}' creada correctamente". format(categoria))
        
    conexion.commit()
    conexion.close()

def agregar_plato():
    conexion = sqlite3.connect("restaurante.bd")
    cursor = conexion.cursor()
    
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Slecciona una categoria para añadir un plato:\n")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))
    
    conexion.commit()
    conexion.close()
    

#Crear la base de datos
create_db()

#Menu de opciones

while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input("\nIntraduce una opcion\n [1] Agregar una categoria\n [2] Agregar Plato\n [3]Salir del Programa\n")
    
    if opcion == "1":
        crear_categoria()
        
    elif opcion == "2":
        agregar_plato()
        
    elif opcion == "3":
        break
    else:
        print("Opcione Incorrecta, las opciones son 1, 2 y 3")