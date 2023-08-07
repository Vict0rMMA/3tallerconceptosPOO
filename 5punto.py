import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((self.centro.x - punto.x) ** 2 + (self.centro.y - punto.y) ** 2)
        return distancia_centro_punto <= self.radio

centro = Punto(0, 0)
radio = 5

circulo1 = Circulo(centro, radio)
print("Área del círculo:", circulo1.calcular_area())
print("Perímetro del círculo:", circulo1.calcular_perimetro())

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

print("¿El punto (3, 4) pertenece al círculo?", circulo1.punto_pertenece(punto1))  
print("¿El punto (6, 8) pertenece al círculo?", circulo1.punto_pertenece(punto2))  
