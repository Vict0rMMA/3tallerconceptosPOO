class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se depositaron {monto} unidades en la cuenta.")
        else:
            print("El monto del depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print(f"Se retiraron {monto} unidades de la cuenta.")
        else:
            print("Fondos insuficientes para realizar el retiro o el monto del retiro no es válido.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se aplicó una cuota de manejo del 2%: {cuota_manejo} unidades.")

    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance} unidades")

cuenta1 = CuentaBancaria("1234567890", ["Juan", "María"], 5000.0)

cuenta1.mostrar_detalles()
cuenta1.depositar(1000.0)
cuenta1.mostrar_detalles()
cuenta1.retirar(3000.0)
cuenta1.mostrar_detalles()
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()
