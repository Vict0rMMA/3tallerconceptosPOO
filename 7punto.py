class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

cuenta1 = CuentaBancaria("1234567890", ["Juan", "María"], 5000.0)
cuenta2 = CuentaBancaria("9876543210", ["Pedro"], 10000.0)

print("Cuenta 1:")
print("Número de cuenta:", cuenta1.numero_cuenta)
print("Propietarios:", cuenta1.propietarios)
print("Balance:", cuenta1.balance)

print("\nCuenta 2:")
print("Número de cuenta:", cuenta2.numero_cuenta)
print("Propietarios:", cuenta2.propietarios)
print("Balance:", cuenta2.balance)
