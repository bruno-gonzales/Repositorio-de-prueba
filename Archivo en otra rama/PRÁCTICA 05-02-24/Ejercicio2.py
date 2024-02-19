empleados = []

def añadirEmpleado():
    idEmpleado = len(empleados)+1
    nombreEmpleado = input("Inserte el nombre del empleado: ")
    departamentoEmpleado = input("Inserte el departamento del empleado: ")
    salarioEmpleado = float(input("Inserte el salario del empleado: "))
    empleados.append([idEmpleado, nombreEmpleado, departamentoEmpleado, salarioEmpleado])
    print("EMPLEADO AGREGADO!")
    input("Presione cualquier botón para continuar.")

def eliminarEmpleado():
    global empleados
    print("ID\tNombre\tDepartamento\tSalario")
    for empleado in empleados:
        print(f"{empleado[0]} --- {empleado[1]} --- {empleado[2]} --- {empleado[3]}")
    id = int(input("Ingrese el ID del empleado a eliminar: "))
    for empleado in empleados:
        if empleado[0] == id:
            empleados.remove(empleado)
            print("EMPLEADO ELIMINADO!")
    input("Presione cualquier botón para continuar.")

def mostarEmpleado():
    print("ID\tNombre\tDepartamento\tSalario")
    for empleado in empleados:
        print(f"ID: {empleado[0]} --- Nombre: {empleado[1]} --- Departamento: {empleado[2]} --- Salario: {empleado[3]}")

def buscarEmpleado():
    buscar_id_nombre = input("Ingrese el nombre o ID del empelado: ")
    global empleados
    for empleado in empleados:
        if empleado[0] == int(buscar_id_nombre) or empleado[1] == buscar_id_nombre:
            print("Empleado encontrado")
            print(f"ID: {empleado[0]} --- Nombre: {empleado[1]} --- Departamento: {empleado[2]} --- Salario: {empleado[3]}")

def salarioPromedioDepartamento():
    departamento = input("Ingrese el departamento: ")

    empleados_departamento = [empleado for empleado in empleados if empleado[2] == departamento]
    if len(empleados_departamento) == 0:
        print("No hay empleados en el departamento")
        return
    salario_promedio = sum(empleado[3] for empleado in empleados_departamento) / len(empleados_departamento)
    print(f"El salario promedio del departamento {departamento} es {salario_promedio}")

def salarioPromedioGeneral():
    salario_promedio = sum(empleado[3] for empleado in empleados) / len(empleados)
    print(f"El salario promedio general es {salario_promedio}")

def menu():
    print("REGISTRO DE EMPLEADOS Y SALARIOS")
    print("1. Agregar empleado.\n2. Eliminar empleado.\n3. Mostrar todos los empleados.\n4. Buscar empleado por ID o nombre.\n5. Calcular salario promedio por departamento.\n6. Calacular salario promedio general.\n7. Salir.")

def main():
    while True:
        menu()
        opcionElegida = int(input("Inserte la opcion a elegir: "))

        if opcionElegida == 7:
            break
        elif opcionElegida == 1:
            añadirEmpleado()
        elif opcionElegida == 2:
            eliminarEmpleado()
        elif opcionElegida == 3:
            mostarEmpleado()
        elif opcionElegida == 4:
            buscarEmpleado()
        elif opcionElegida == 5:
            salarioPromedioDepartamento()
        elif opcionElegida == 6:
            salarioPromedioGeneral()

main()