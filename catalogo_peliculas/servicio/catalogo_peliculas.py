import os

class CatalogoPeliculas:
  ruta_archivo = 'peliculas.txt'
  
  @staticmethod
  def agregar_pelicula(pelicula):
    try:
      archivo = open(CatalogoPeliculas.ruta_archivo, "a")
      archivo.write(pelicula.get_nombre() + "\n")
    except Excepction as e:
      print("Error: " + e)
    finally:
      archivo.close()
  
  @staticmethod
  def listar_peliculas():
    try:
      archivo = open(CatalogoPeliculas.ruta_archivo, "r")
      print(archivo.read())
    except Excepction as e:
      print("Error: " + e)
    finally:
      archivo.close()
  
  @staticmethod
  def eliminar_catalogo():
    try:
      os.remove(CatalogoPeliculas.ruta_archivo)
    except Excepction as e:
      print("Error: " + e)
    