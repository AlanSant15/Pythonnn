#Crea un programaen python para INSUCO STREAMING

#Ingresar N peliculas
#Cada pelicula tiene (nombre de la pelicula, protagonista, antagonista, director, genero, año deestreno, cantidad de visualizacionn o vistas)
#Crea una funcion para validar GENERO (Accion, Terror, Comedia, Romance, Infantil)
#Crea otra funcion para validar AÑO(2000-2024)
#Mostrar pelicula mas vista
#Mostrar pelicula menos vista
#Calcular promedio devisualizaciones o vistas
#Sumar cantidad de peliculas de accion, y almacenarlas en un nuevo ARRAY
#Se debe implementar ARRAY O ARREGLO

class Pelicula:
    def __init__(self, nombre, protagonista, antagonista, director, genero, año, visualizaciones):
        self.nombre = nombre
        self.protagonista = protagonista
        self.antagonista = antagonista
        self.director = director
        self.genero = genero
        self.año = año
        self.visualizaciones = visualizaciones

def validar_genero(genero):
    generos_validos = ["Acción", "Comedia", "Drama", "Terror", "Aventuras"]
    return genero in generos_validos

def validar_año(año):
    return isinstance(año, int) and 2000 <= año <= 2024

def crear_arreglo_peliculas():
    arreglo_peliculas = []
    num_peliculas = int(input("Ingrese número de películas: "))
    print("")

    for i in range(num_peliculas):
        nombre = input(f"Ingrese nombre de película {i+1}: ")
        protagonista = input(f"Ingrese protagonista de película {i+1}: ")
        antagonista = input(f"Ingrese antagonista de película {i+1}: ")
        director = input(f"Ingrese director de película {i+1}: ")
        genero = input(f"Ingrese género de película {i+1} (Acción, Comedia, Drama, Terror, Aventuras): ")

        while not validar_genero(genero):
            genero = input(f"Error: Género inválido. Ingrese género de película {i+1} (Acción, Comedia, Drama, Terror, Aventuras): ")

        año = int(input(f"Ingrese año de estreno de película {i+1}: "))

        while not validar_año(año):
            año = int(input(f"Error: Año inválido. Ingrese año de estreno de película {i+1} (1900-2024): "))

        visualizaciones = int(input(f"Ingrese visualizaciones de película {i+1}: "))

        pelicula = Pelicula(nombre, protagonista, antagonista, director, genero, año, visualizaciones)
        arreglo_peliculas.append(pelicula)
        print("****************************************************")
        print("")
    return arreglo_peliculas

def mostrar_pelicula_mas_vista(arreglo_peliculas):
    max_visualizaciones = max(pelicula.visualizaciones for pelicula in arreglo_peliculas)
    pelicula_mas_vista = next(pelicula for pelicula in arreglo_peliculas if pelicula.visualizaciones == max_visualizaciones)

    print(f"Película más vista: {pelicula_mas_vista.nombre} ({pelicula_mas_vista.visualizaciones} visualizaciones)")
    print("")

def mostrar_pelicula_menos_vista(arreglo_peliculas):
    min_visualizaciones = min(pelicula.visualizaciones for pelicula in arreglo_peliculas)
    pelicula_menos_vista = next(pelicula for pelicula in arreglo_peliculas if pelicula.visualizaciones == min_visualizaciones)

    print(f"Película menos vista: {pelicula_menos_vista.nombre} ({pelicula_menos_vista.visualizaciones} visualizaciones)")
    print("")

def calcular_promedio_visualizaciones(arreglo_peliculas):
    total_visualizaciones = sum(pelicula.visualizaciones for pelicula in arreglo_peliculas)
    promedio_visualizaciones = total_visualizaciones / len(arreglo_peliculas)

    print(f"Promedio de visualizaciones: {promedio_visualizaciones:.2f}")
    print("")

arreglo_peliculas = crear_arreglo_peliculas()

mostrar_pelicula_mas_vista(arreglo_peliculas)
mostrar_pelicula_menos_vista(arreglo_peliculas)
calcular_promedio_visualizaciones(arreglo_peliculas)
print("")

