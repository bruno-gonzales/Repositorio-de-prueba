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