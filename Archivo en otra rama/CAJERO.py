#CAJERO
#1.Consultas Saldo
#2.Retiro
#3.Depósito
#4.Salir

saldoUsuario = float(input("SALDO USUARIO : S/."))

print("Bienvenido al cajero!")
print("\n1.Consultar Saldo.\n2.Retiro.\n3.Depósito.\n4.Salir")
opcionUsuario = int(input("Opción   :   "))

if opcionUsuario == 1:
    print("\n1.Consultar Saldo.")
    print(f"SALDO USUARIO : S/.{saldoUsuario}")
elif opcionUsuario == 2:
    print("\n2.Retiro.")
    retiroSaldo = float(input("Retiro de Saldo : S/."))
    if retiroSaldo <= saldoUsuario:
        saldoUsuario -= retiroSaldo
        print(f"SALDO USUARIO : S/.{saldoUsuario}")
    else:
        print("ERROR! SALDO NO DISPONIBLE")
elif opcionUsuario == 3:
    print("\n3.Depósito")
    depositoBillete10 = int(input("Cantidad de billetes de S./10"))
    depositoBillete20 = int(input("Cantidad de billetes de S./20"))
    depositoBillete50 = int(input("Cantidad de billetes de S./50"))
    depositoBillete100 = int(input("Cantidad de billetes de S./100"))
    depositoSaldo = 1
    if (depositoBillete10, depositoBillete20,depositoBillete50) < 0:
        print("esoo esta mal")
    if depositoSaldo > 0:
        saldoUsuario += depositoSaldo
        print(f"SALDO USUARIO : S/.{saldoUsuario}")
    else:
        print("ERROR! DEPÓSITO NO DISPONIBLE")
else:
    print("\nSALIR")

#METODO OFICIAL
print("Cajero automático")
print("1. Mostrar saldo.\n2. Ingresar dinero a la cuenta.")
opcionElegida = int(input("Ingrese una opcion: "))
saldo = 0
billetesPosibles = [10,20,50,100,200]
billetesIngresados = []

if opcionElegida == 1:
    print("Usted tiene " + str(saldo) + " soles")
elif opcionElegida == 2:
    for i in range(len(billetesPosibles)):
            billetesIngresados.append(int(input(f'Cuantos billetes de S./{str(billetesPosibles[i])} va a ingresar: ')))
    print("Gracias por su transaccion")
    for i in range(len(billetesPosibles)):
            saldo += billetesIngresados[i]*int(billetesPosibles[i])
    print("Usted tiene " + str(saldo) + " soles")

#CON FUNCIONES

def menu():
    print("Cajero automático")
    print("1. Mostrar saldo.\n2. Ingresar dinero a la cuenta.")
    opcionElegida = int(input("Ingrese una opcion: "))
    opciones(opcionElegida)

def opciones(opcionElegida):
    if opcionElegida == 1:
        mostrarSaldo(saldo)
    elif opcionElegida == 2:
        ingresarDinero(saldo)
    menu()

def mostrarSaldo(saldo):
    print("Usted tiene " + str(saldo) + " soles")
    input("Pulse cualquier tecla para volver al menu")
    menu()

def ingresarDinero(saldo):
    billetesPosibles = [10,20,50,100,200]
    billetesIngresados = []
    for i in range(len(billetesPosibles)):
            billetesIngresados.append(int(input("Cuantos billetes de S./" + str(billetesPosibles[i]) + " va a ingresar: ")))
    print("Gracias por su transaccion")
    for i in range(len(billetesPosibles)):
            saldo += billetesIngresados[i]*int(billetesPosibles[i])
    print("Usted tiene " + str(saldo) + " soles")
    input("Pulse cualquier tecla para volver al menu")
    return saldo
saldo = 0
opcionElegida = menu()