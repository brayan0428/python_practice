class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "El vehiculo es de color " + self.color + ", tiene " + str(self.ruedas) + " ruedas" 

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        Vehiculo.__init__(self,color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return Vehiculo.__str__(self) + " y corre a una velocidad de " + str(self.velocidad) + " km/h"
        
class Bicicleta(Vehiculo):
  def __init__(self, color, ruedas, tipo):
    Vehiculo.__init__(self,color,ruedas)
    self.tipo = tipo
  
  def __str__(self):
    return Vehiculo.__str__(self) + " y es una bicicleta de tipo " + self.tipo
    
coche = Coche("Rojo", 4, 20)
print(coche)

bicicleta = Bicicleta("Negra",2,"montaña")
print(bicicleta)