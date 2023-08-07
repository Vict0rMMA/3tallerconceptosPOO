class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        return base == altura

# Ejemplo de uso de la clase Rectángulo
esquina_sup_izq = Punto(1, 4)
esquina_inf_der = Punto(5, 1)

rectangulo1 = Rectángulo(esquina_sup_izq, esquina_inf_der)
print("Perímetro del rectángulo:", rectangulo1.calcular_perimetro())
print("Área del rectángulo:", rectangulo1.calcular_area())
print("¿El rectángulo es un cuadrado?", rectangulo1.es_cuadrado())
