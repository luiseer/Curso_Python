class Pelicula():
    #constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se a cerado la pelicula", self.titulo)
    #destructor de clase
    
    def __del__(self):
        print("Se esta borrando la pelicula ", self.titulo)

p = Pelicula("Casa blanca", 180, "1987")
del(p)