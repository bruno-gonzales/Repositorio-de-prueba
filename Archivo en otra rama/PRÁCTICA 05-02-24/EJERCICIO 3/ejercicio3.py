'''Ejercicio 3: Simulador de Reservas de Asientos en Cine
Descripción: Crea un simulador para la reserva de asientos en una sala de cine. La 
sala de cine debe ser representada por una matriz (lista de listas), donde cada elemento 
puede estar vacío (disponible) o reservado. El sistema debe permitir visualizar los 
asientos, realizar reservas, cancelar reservas y mostrar estadísticas de ocupación.
Funcionalidades:
• Visualizar asientos
• Realizar reserva de asiento
• Cancelar reserva de asiento
• Mostrar estadísticas de ocupación (porcentaje de asientos ocupados, asientos 
disponibles
'''

asientos = []
for i in range(1,51):
    asientos.append([i, "disponible"])

def visualizar_asientos():
    for asiento in asientos:
        print(asiento)

def realizar_reserva():
    global asientos
    asiento_reserva = int(input("Ingrese el numero de asiento a revervar: "))
    for asiento in asientos:
        if asiento[0] == asiento_reserva:
            if asiento[1] == "disponible":
                asiento[1] = "reservado"
                print("Asiento reservado")
            else:
                print("Asiento ocupado")

def cancelar_reserva():
    global asientos
    asiento_cancelado = int(input("Ingrese el numero de asiento a cancelar reserva: "))
    for asiento in asientos:
        if asiento[0] == asiento_cancelado:
            if asiento[1] == "reservado":
                asiento[1] = "disponible"
                print("Reserva cancelada")
            else:
                print("ERROR-ASIENTO DISPONIBLE")

def estadisticas_ocupacion():
    global asientos
    asientos_disponibles = 0
    asientos_reservados = 0
    for asiento in asientos:
        if asiento[1] == "disponible":
            asientos_disponibles += 1
        else:
            asientos_reservados += 1

    porcentaje_disponibles = (asientos_disponibles/50)*100
    porcentaje_reservados = (asientos_reservados/50)*100

    print(f"Reservados: {porcentaje_reservados}%\nDisponibles: {porcentaje_disponibles}%")

def mostrar_menu():
    print("1. Visualizar asientos")
    print("2. Realizar reservas de asientos")
    print("3. Cancelar reserva de asiento")
    print("4. Mostrar estadísticas de ocupacion")
    print("5. Salir")

def main():
    while True:
        print()
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))
        while opcion <= 0 or opcion > 5:
            opcion = int(input("Ingrese una opcion: "))
        if opcion == 5:
            break
        elif opcion == 1:
            visualizar_asientos()    
        elif opcion == 2:
            realizar_reserva()
        elif opcion == 3:
            cancelar_reserva()  
        elif opcion == 4:
            estadisticas_ocupacion()

if __name__ == "__main__":
    main()

