import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
#                     dni VARCHAR(9) PRIMARY KEY,
#                     nombre VARCHAR(100), 
#                     edad INTEGER,
#                     email VARCHAR(100))''')

# usuarios = [
#     ('11111111A','Hugo', 26, 'hugo@mail.com'),
#     ('22222222B','Francisco', 46, 'frnacisco@mail.com'),
#     ('33333333C','Luis', 16, 'luis1@mail.com'),
#     ('44444444D','Sandra', 26, 'sandra@mail.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
#                 id INTEGER PRIMARY KEY  AUTOINCREMENT,
#                 nombre VARCHAR(100) NOT NULL,
#                 marca VARCHAR(50) NOT NULL,
#                 precio FLOAT NOT NULL)
#               ''')

# productos = [
#     ('Teclado', 'Logitech', 19.95),
#     ('Pantalla', 'LG', 89.95)
# ]

# cursor.executemany(
#     "INSERT INTO productos VALUES (NULL, ?,?,?)", productos
# )

# cursor.execute(
#     "SELECT * FROM productos"
# )

# productos = cursor.fetchall()

# for producto in productos:
#     print('Nombre: ', producto[1], 'Precio: ', producto[3] )



cursor.execute('''CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni VARCHAR(9) UNIQUE,
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
)
               ''')

usuarios = [
    ('11111111A','Hugo', 26, 'hugo@mail.com'),
    ('22222222B','Francisco', 46, 'frnacisco@mail.com'),
    ('33333333C','Luis', 16, 'luis1@mail.com'),
    ('44444444D','Sandra', 26, 'sandra@mail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (NULL,?,?,?,?)", usuarios)

conexion.commit()
conexion.close()