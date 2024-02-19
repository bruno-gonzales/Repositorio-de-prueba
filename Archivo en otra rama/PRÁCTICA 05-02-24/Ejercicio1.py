productos = []

def agregarProducto():
    idProducto = len(productos)+1
    nombreProducto = input("Inserte el nombre del producto: ")
    cantidadProducto = int(input("Inserte la cantidad del producto: "))
    precioProducto = float(input("Inserte el precio del producto: "))
    productos.append([idProducto, nombreProducto, cantidadProducto, precioProducto])
    print("PRODUCTO AGREGADO!")
    input("Presione cualquier botón para continuar.")

def eliminarProducto():
    global productos
    print("ID\tNombre\tCantidad\tPrecio")
    for producto in productos:
        print(f"{producto[0]}\t{producto[1]}\t{producto[2]}\t{producto[3]}")
    id = int(input("Ingrese el ID del producto a eliminar: "))
    for producto in productos:
        if producto[0] == id:
            productos.remove(producto)
            print("PRODUCTO ELIMINADO!")
    input("Presione cualquier botón para continuar.")

def actualizarProducto():
    global productos
    print("ID\tNombre\tCantidad\tPrecio")
    for producto in productos:
        print(f"{producto[0]}\t{producto[1]}\t{producto[2]}\t{producto[3]}")
    id = int(input("Ingrese el ID del producto a actualizar: "))
    for producto in productos:
        if producto[0] == id:
            producto[1] = input("Inserte el nombre del producto: ")
            producto[2] = int(input("Inserte la cantidad del producto: "))
            producto[3] = float(input("Inserte el precio del producto: "))
            print("Producto actualizado")

def buscarProducto():
    buscar_id_nombre = input("Ingrese el nombre o ID del producto: ")
    global productos
    for producto in productos:
        if producto[0] == int(buscar_id_nombre) or producto[1] == buscar_id_nombre:
            print("Producto encontrado")
            print(f"ID: {producto[0]} --- Nombre: {producto[1]} --- Cantidad: {producto[2]} --- Precio: {producto[3]}")

def valorTotalInventario():
    global productos

    sumTotal = 0

    for producto in productos:
        sumTotal += producto[2]*producto[3]

    return sumTotal

def menu():
    print("GESTION DE INVENTARIO")
    print("1. Agregar producto.\n2. Eliminar producto.\n3. Actualizar producto.\n4. Buscar producto por ID o nombre.\n5. Calcular valor total de inventario.\n6. Salir.")

def main():
    while True:
        menu()
        opcionElegida = int(input("Inserte la opcion a elegir: "))

        if opcionElegida == 6:
            break
        elif opcionElegida == 1:
            agregarProducto()
        elif opcionElegida == 2:
            eliminarProducto()
        elif opcionElegida == 3:
            actualizarProducto()
        elif opcionElegida == 4:
            buscarProducto()
        elif opcionElegida == 5:
            print(f"El valor total del Inventario es: s/{calcularValorInventario()}")

main()