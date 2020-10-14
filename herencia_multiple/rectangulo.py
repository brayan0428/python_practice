from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica,Color):
  def __init__(self, ancho, alto, color):
    FiguraGeometrica.__init__(self, ancho, alto)
    Color.__init__(self, color)
    
  def area(self):
    return self.get_ancho() * self.get_alto()
  
  def __str__(self):
    return "El area del rectangulo es: " + str(self.area()) + " y es de color " + self.get_color()