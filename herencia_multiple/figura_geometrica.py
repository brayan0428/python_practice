class FiguraGeometrica:
  def __init__(self,alto,ancho):
    self.__alto = alto
    self.__ancho = ancho
  
  def get_alto(self):
    return self.__alto
  
  def get_ancho(self):
    return self.__ancho
  
  def set_alto(self, alto):
    self.__alto = alto
  
  def set_ancho(self, ancho):
    self.__ancho = ancho