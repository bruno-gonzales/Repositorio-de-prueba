tareas = []

def añadirTarea():
    numeroTarea = len(tareas)+1
    nuevaTarea = input("Inserte una nueva tarea: ")
    tareas.append([numeroTarea, nuevaTarea])
    print("TAREA AÑADIDA!")
    input("Presione cualquier botón para continuar.")

def eliminarTarea():
    print("TAREAS A HACER:")
    for tarea in tareas:
        print(f"{tarea[0]}. {tarea[1]}")
    numero = int(input("Ingrese el numero de la tarea a eliminar: "))
    for tarea in tareas:
        if tarea[0] == numero:
            tareas.remove(tarea)
            print("TAREA ELIMINADA!")
    input("Presione cualquier botón para continuar.")

def mostrarTareas():
    print("TAREAS A HACER:")
    for tarea in tareas:
        print(f"{tarea[0]}. {tarea[1]}")
    input("Presione cualquier botón para continuar.")

def tareaCompleta():
    print("TAREAS A HACER:")
    for tarea in tareas:
        print(f"{tarea[0]}. {tarea[1]}")
    numero = int(input("Ingrese el numero de la tarea a marcar como completa: "))
    for tarea in tareas:
        if tarea[0] == numero:
            tarea[1] = f"{tarea[1]} (COMPLETA)"
            print("Tarea marcada como completa exitosamente!")
    input("Presione cualquier botón para continuar.")

def menu():
    print("ADMINISTRADOR DE TAREAS")
    print("1. Añadir tarea.\n2. Eliminar tarea.\n3. Mostrar todas las tareas.\n4. Marcar tarea como completada.\n5. Salir.")

def main():
    while True:
        menu()
        opcionElegida = int(input("Inserte la opcion a elegir: "))

        if opcionElegida == 5:
            break
        elif opcionElegida == 1:
            añadirTarea()
        elif opcionElegida == 2:
            eliminarTarea()
        elif opcionElegida == 3:
            mostrarTareas()
        elif opcionElegida == 4:
            tareaCompleta()

main()