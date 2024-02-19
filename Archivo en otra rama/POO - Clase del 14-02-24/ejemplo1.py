class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}")

persona1 = Persona("Juan", 30, "Mexicana")
persona2 = Persona("Maria", 25, "Colombiana")
persona3 = Persona("Pedro", 27, "Argentina")

print(persona1)
print(persona2)
print(persona3)

class Animal:
    def __init__(self, nombre, cantPatas, especie):
        self.nombre = nombre
        self.cantPatas = cantPatas
        self.especie = especie
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Cantidad de patas: {self.cantPatas}, Especie: {self.especie}")

animal1 = Animal("Perro", 4, "Mamífero")
animal2 = Animal("Avestruz", 2, "Ave")
animal3 = Animal("Tarántula", 8, "Arácnido")

print(animal1)
print(animal2)
print(animal3)

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}")

producto1 = Producto("Chifle", 120, 1.00)
producto2 = Producto("Inca Kola", 150, 2.50)
producto3 = Producto("Leche", 200, 4.50)

print(producto1)
print(producto2)
print(producto3)

class Ropa:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Marca: {self.marca}, Precio: {self.precio}")

ropa1 = Ropa("Polera", "Gucci", 349.90)
ropa2 = Ropa("Zapatillas", "Nike", 579.90)
ropa3 = Ropa("Pantalón", "Louis Vuitton", 1300.00)

print(ropa1)
print(ropa2)
print(ropa3)