class Carta:
    PINTA_CORAZON = 'Corazón'
    PINTA_DIAMANTE = 'Diamante'
    PINTA_TREBOL = 'Trébol'
    PINTA_ESPADA = 'Espada'

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta(7, Carta.PINTA_CORAZON)
carta2 = Carta(10, Carta.PINTA_TREBOL)

print("Carta 1:", carta1.valor, carta1.pinta)
print("Carta 2:", carta2.valor, carta2.pinta)  
