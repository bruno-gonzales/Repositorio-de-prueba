def saludar(nombre):
    print ("Hola", nombre)

def despedir(nombre):
    return print("Adios", nombre)

saludar("Bruno")
despedir("Jorge")

#MULTIPLES PARAMETROS

def calcularAreaTriangulo(base, altura):
    return base * altura / 2

print(calcularAreaTriangulo(3, 4))

#EJERCICIO 1

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2 if num2 != 0 else "Error: Division por cero"

def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == "5":
            break
        
        elif opcion in [1,2,3,4]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            if opcion == 1:
                print("La suma es: ", sumar(num1, num2))
            if opcion == 2:
                print("La resta es: ", restar(num1, num2))
            if opcion == 3:
                print("La multiplicacion es: ", multiplicar(num1, num2))
            if opcion == 4:
                print("La division es: ", dividir(num1, num2))
        else:
            print("Opcion invalida")
        input("Pulse cualquier tecla para volver")

if __name__ == "__main__":
    main()

#EJERCICIO 2
empleados = []

def agregar_empleado():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    cargo_empleado = input("Ingrese el cargo del empleado: ")
    empleados.append([nombre_empleado, cargo_empleado])

def ver_empleado():
    for empleado in empleados:
        print("Empleado: " + str(empleado[0]) + " --- Cargo: " + str(empleado[1]))

def eliminar_empleado():
    nombre_empleado = input("Ingrese el nombre del empleado a eliminar: ")
    global empleados
    empleados = [empleado for empleado in empleados if empleado[0] != nombre_empleado]

def mostrar_menu():
    print("1. Agregar empleados")
    print("2. Ver empleados")
    print("3. Borrar empleados")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == "4":
            break
        elif opcion == 1:
            agregar_empleado()
        elif opcion == 2:
            ver_empleado()
        elif opcion == 3:
            eliminar_empleado()
        else:
            print("Opcion invalida")
        input("Pulse cualquier tecla para volver")

if __name__ == "__main__":
    main()