import sqlite3

conexion = sqlite3.connect("ejemplo.db")

if conexion:
    print("conexión exitosa")
else:
    print("No fue posible realizar la conexion")
    
cursor = conexion.cursor()

# cursor.execute(
#     "CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))"
# )

# cursor.execute(
#     "INSERT INTO usuarios VALUES('Luis',36,'luiseer09@gmail.com')"
# )

# cursor.execute(
#     "SELECT * FROM usuarios"
# )
# print(cursor)

# usuario = cursor.fetchone()
# print(usuario[0])

# usuarios = [
#     ('Hugo', 26, 'hugo@mail.com'),
#     ('Francisco', 46, 'frnacisco@mail.com'),
#     ('Luis', 16, 'luis1@mail.com'),
#     ('Sandra', 26, 'sandra@mail.com')
# ]

# cursor.executemany(
#     "INSERT INTO usuarios VALUES (?,?,?)", usuarios
# )

cursor.execute(
    "SELECT * FROM usuarios"
)

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conexion.commit()
conexion.close()