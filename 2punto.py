class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

punto1 = Punto(3, 5)
print("Coordenadas del punto:", punto1) 
