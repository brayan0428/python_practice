from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

salir = False

def procesar(opcion):
  if opcion == "1":
    nueva_pelicula()
  if opcion == "2":
    global catalogo
    CatalogoPeliculas.listar_peliculas()
  if opcion == "3":
    CatalogoPeliculas.eliminar_catalogo()
  if opcion == "4":
    global salir
    salir = True

def nueva_pelicula():
  nombre_pelicula = input("Ingrese el nombre de la película: ")
  pelicula = Pelicula(nombre_pelicula)
  CatalogoPeliculas.agregar_pelicula(pelicula)
  del pelicula
  
while not salir:
  print("""
    Seleccione la opción: 
      1. Agregar película
      2. Listar peliculas
      3. Eliminar catalogo de películas
      4. Salir
  """)
  
  opcion = input("Escoge tu opción (1-4): ")
  procesar(opcion)
    
    