def consultarSaldo(saldo):
    print(f"SALDO USUARIO : S/.{saldo}")


def retirarSaldo(saldo):
    retiro = int(input("RETIRO : S/."))

    while retiro > saldo or retiro < 0:
        print("!ERROR! --> SALDO NO DISPONIBLE")
        retiro = int(input("RETIRO : S/."))

    print("!RETIRO SATISFACTIORIO!")
    return retiro


def depositoSaldo():
    tiposBilletes = [10, 20, 50, 100, 200]
    montoBillete = []
    deposito = 0

    for numero in tiposBilletes:
        cantidadBilletes = int(input(f"CANTIDAD DE BILLETES DE S/.{numero} A DEPOSITAR : "))
        while cantidadBilletes < 0:
            print("!ERROR! --> CANTIDAD NEGATIVA")
            cantidadBilletes = int(input(f"CANTIDAD DE BILLETES DE S/.{numero} A DEPOSITAR : "))
        montoBillete.append(numero*cantidadBilletes)

    print("!DEPÓSITO SATISFACTORIO!")
    print(f"DEPÓSITO ACTUAL  : S/.{sum(montoBillete)}")

    deposito += sum(montoBillete)
    return deposito


#CÓDIGO PRINCIPAL

saldoUsuario = 0

print("\n1.Consultar Saldo.\n2.Retiro.\n3.Depósito.\n4.Salir")
opcionUsuario = int(input("Opción   :   "))

while opcionUsuario < 0 or opcionUsuario > 4:
    print("!ERROR! --> OPCIÓN INCORRECTA.")
    opcionUsuario = int(input("Opción   :   "))

while opcionUsuario != 4:
    if opcionUsuario == 1:
        print("\n1.CONSULTAR SALDO")
        consultarSaldo(saldoUsuario)
        input("Pulse cualquier botón para continuar")
    elif opcionUsuario == 2:
        print("\n2.RETIRAR SALDO")
        saldoUsuario -= retirarSaldo(saldoUsuario)
        input("Pulse cualquier botón para continuar")
    elif opcionUsuario == 3:
        print("\n3.DEPÓSITAR SALDO")
        saldoUsuario += depositoSaldo()
        input("Pulse cualquier botón para continuar")

    print("\n1.Consultar Saldo.\n2.Retiro.\n3.Depósito.\n4.Salir")
    opcionUsuario = int(input("Opción   :   "))
    while opcionUsuario < 0 or opcionUsuario > 4:
        print("!ERROR! --> OPCIÓN INCORRECTA.")
        opcionUsuario = int(input("Opción   :   "))

print("!\nGRACIAS POR USAR NUESTROS SERVICIOS!")

#METODOS -----> FUNCIONES
