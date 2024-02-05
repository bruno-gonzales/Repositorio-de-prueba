#while condicion:

#EJEMPLO 1:
contador = 0

while contador < 5:
    print(contador)
    contador += 1

#EJEMPLO 2: Lista de compras
cantidadProductos = int(input("Ingrese la cantidad de productos: "))
listaProductos = []
precioProductos = []

while cantidadProductos <= 0:
    print("No se puede trabajar con ese numero")
    cantidadProductos = int(input("Ingrese nuevamente la cantidad de productos: "))

for i in range(cantidadProductos):
    producto = input("Ingrese el producto n°"+ str(i+1) + ": ")
    precio = float(input("Ingrese el precio del producto n°"+ str(i+1) + ": S./"))
    while precio < 0:
        print("No se puede trabajar con ese numero")
        precio = float(input("Ingrese el precio del producto n°"+ str(i+1) + ": S./"))
    listaProductos.append([producto, precio])
    print("Producto registrado")
for producto in listaProductos:
    print("Producto: " + str(producto[0]) + "- Precio: S./" + str(producto[1]))

#FUNCIONES

#def nombre_funcion()
#nombre_funcion()