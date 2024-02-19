#Ejercicio 1: CuentaBancaria
#Crea una clase llamada CuentaBancaria que tenga los siguientes atributos y métodos:

#Atributos: titular(Nombre del titular de la cuenta) y saldo
#Métodos:
#__init__(self, titular, saldo): Constructor de la clase
#depositar(self, cantidad): Método para depositar dinero en la cuenta
#retirar(self, cantidad): Método para retirar dinero de la cuenta. Si la cantidad a retirar es mayor que el saldo, imprime mensaje de error.
#mostrar_saldo(self): Método para mostrar el saldo actual de la cuenta.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= cantidad
            
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta1 = CuentaBancaria("Juan", 1000)
cuenta1.depositar(500)
cuenta1.mostrar_saldo()