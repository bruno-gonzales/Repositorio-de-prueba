import random

def crear_cine(filas, columnas):
    opcionAsiento = [None, "R"]
    asientos = [[random.choice(opcionAsiento) for i in range(columnas)] for i in range(filas)] # Se delimita la matriz de asientos
    reservaciones = [] # Creamos una lista vacia para las reservaciones.
    return asientos, reservaciones # Devolvemos dichos valores.

def visualizar_asientos(asientos):
    for fila in asientos: # Se hace una lectura asiento por asiento para ver si esta reservado o disponible.
        print(" ".join(["\tO" if asiento is None else "\tR" for asiento in fila]))

def reservar_asiento(asiento, reservaciones, fila, columna):
    if asiento[fila][columna] is None:
        asiento[fila][columna] = "R"
        reservaciones.append((fila, columna))
        return True
    else:
        return False

def cancelar_reservacion(asientos, reservaciones, fila, columna):
    if asientos[fila][columna] == "R":
        asientos[fila][columna] = None
        reservaciones.remove((fila, columna))
        return True
    else:
        return False

def estadisticas(asientos):
    reservado = sum(1 for fila in asientos for asiento in fila if asiento is not None)
    disponible = sum(1 for fila in asientos for asiento in fila if asiento is None)
    porcentaje_reservado = (reservado / (len(asientos) * len(asientos[0]))) * 100
    return reservado, disponible, porcentaje_reservado

def menu(asientos, reservaciones):
    while True:
        print("\n1. Visualizar asientos")
        print("2. Reservar asiento")
        print("3. Cancelar reservación")
        print("4. Estadísticas")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            visualizar_asientos(asientos)
        elif opcion == 2:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))
            reservar_asiento(asientos, reservaciones, fila -1 , columna -1 )
        elif opcion == 3:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))
            cancelar_reservacion(asientos, reservaciones, fila - 1, columna - 1)
        elif opcion == 4:
            reservado, disponible, porcentaje_reservado = estadisticas(asientos)
            print(f"Asientos reservados: {reservado}")
            print(f"Asientos disponibles: {disponible}")
            print(f"Porcentaje de reservacion: {porcentaje_reservado:.2f}%")
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Crear una sala de cine con n filas y n columnas:
asientos, reservaciones = crear_cine(10, 10)

# Mostrar el menú
menu(asientos, reservaciones)