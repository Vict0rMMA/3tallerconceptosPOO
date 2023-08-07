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

cuenta1 = CuentaBancaria("1234567890", ["Juan", "María"], 5000.0)

print("Balance inicial:", cuenta1.balance)
cuenta1.depositar(1000.0)
print("Nuevo balance:", cuenta1.balance)
cuenta1.depositar(-500)  
