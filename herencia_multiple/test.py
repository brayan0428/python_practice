from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado = Cuadrado(5,'rojo')
print(cuadrado.get_color())
cuadrado.set_color('verde')
print(cuadrado.get_color())
print(cuadrado)

rectangulo = Rectangulo(10,5,'naranja')
print(rectangulo)