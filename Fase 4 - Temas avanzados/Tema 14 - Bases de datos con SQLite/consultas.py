import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()




# cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     dni VARCHAR(9) UNIQUE,
#     nombre VARCHAR(100),
#     edad INTEGER,
#     email VARCHAR(100)
# )
#             ''')

usuarios = [
    ('11111111A','Hugo', 26, 'hugo@mail.com'),
    ('22222222B','Francisco', 46, 'frnacisco@mail.com'),
    ('33333333C','Luis', 16, 'luis1@mail.com'),
    ('44444444D','Sandra', 26, 'sandra@mail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (NULL,?,?,?,?)", usuarios)


cursor.execute("SELECT * FROM usuarios WHERE id=1")

conexion.commit()
conexion.close()