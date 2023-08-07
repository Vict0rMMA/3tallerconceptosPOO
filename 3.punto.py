import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

punto1 = Punto(3, 5)
punto2 = Punto(7, 2)

punto1.mostrar() 
punto1.mover(10, 8)
punto1.mostrar()  

distancia_entre_puntos = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia_entre_puntos)  
