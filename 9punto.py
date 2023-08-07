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

cuenta1 = CuentaBancaria("1234567890", ["Juan", "María"], 5000.0)

print("Balance inicial:", cuenta1.balance)
cuenta1.depositar(1000.0)
print("Nuevo balance:", cuenta1.balance)
cuenta1.retirar(3000.0)
print("Nuevo balance después del retiro:", cuenta1.balance)
cuenta1.retirar(4000.0) 
