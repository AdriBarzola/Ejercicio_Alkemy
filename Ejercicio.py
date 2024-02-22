#EJERCICIO: Crear una clase producto que tenga 3 hijos: Libro, pelicula, disco 
#Deben contengar 3 atributos
#metodo mostrar productoque dependiendo el producto va a mostrar diferentes caracteristicas
#Libro pelicula disco cada una debe tener 2 atributos
#3 instancias por clase hijo (3 libros, 3 discos, 3 peliculas)

class Producto:
    def __init__(self, titulo, precio, descripcion):
        self.titulo = titulo
        self.precio = precio
        self.descripcion = descripcion
    
    def mostrar_producto(self):
        pass

class Libro(Producto):
    def __init__(self, titulo, precio, descripcion, autor, genero):
        super().__init__(titulo, precio, descripcion)
        self.autor = autor
        self.genero = genero
    
    def mostrar_producto(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}"

class Pelicula(Producto):
    def __init__(self, titulo, precio, descripcion, director, duracion):
        super().__init__(titulo, precio, descripcion)
        self.director = director
        self.duracion = duracion
    
    def mostrar_producto(self):
        return f"Película: {self.titulo}, Director: {self.director}, Duración: {self.duracion} minutos"

class Disco(Producto):
    def __init__(self, titulo, precio, descripcion, artista, genero):
        super().__init__(titulo, precio, descripcion)
        self.artista = artista
        self.genero = genero
    
    def mostrar_producto(self):
        return f"Disco: {self.titulo}, Artista: {self.artista}, Género: {self.genero}"

#Instancias de clase
libros = [
    Libro("El Señor de los Anillos", 9500, "Fantasía épica", "J.R.R. Tolkien", "Fantasía"),
    Libro("Harry Potter y la Piedra Filosofal", 12300, "Magia y aventura", "J.K. Rowling", "Fantasía"),
    Libro("Cien años de soledad", 10750, "Realismo mágico", "Gabriel García Márquez", "Ficción")
]

peliculas = [
    Pelicula("El Padrino", 3500, "Drama criminal", "Francis Ford Coppola", 175),
    Pelicula("Son como niños", 2700, "Comedia", "Dennis Dugan", 120),
    Pelicula("La La Land", 3200, "Comedia romántica", "Damien Chazelle", 128)
]

discos = [
    Disco("Thriller", 25000, "Álbum más vendido de todos los tiempos", "Michael Jackson", "Pop"),
    Disco("Dark Side of the Moon", 21700, "Álbum icónico de Pink Floyd", "Pink Floyd", "Rock progresivo"),
    Disco("El amor después del amor", 26300, "Uno de los álbumes más vendidos de la historia", "Fito Paez", "Rock")
]

print("Información de los libros:")
for libro in libros:
    print(libro.mostrar_producto())

print("\nInformación de las películas:")
for pelicula in peliculas:
    print(pelicula.mostrar_producto())

print("\nInformación de los discos:")
for disco in discos:
    print(disco.mostrar_producto())