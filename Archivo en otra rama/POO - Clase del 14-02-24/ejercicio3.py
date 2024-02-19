#Implementa polimorfismo:

#1. Crea una clase abstracta Animal con un método abstracto hacer_sonido().
#2. Crea clases concretas que hereden de Animal, por ejemplo, Perro y Gato, e implementa el método hacer_sonido para cada uno de ellos de manera que refleje el sonido específico que hace cada animal.
#3. Demuestra cómo se pueden crear instancias de Perro y Gato y cómo llamar al método hacer_sonido en objetos de ambas clases, mostrando así el polimorfismo.

#CREANDO CLASE ANIMAL
class Animal():
    #CREANDO METODO ABSTRACTO hacer_sonido
    def hacer_sonido(self):
        pass

#CREANDO CLASES CONCRETAS E IMPLEMENTANDO hacer_sonido
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla")

#CREANDO INSTANCIAS
perro1 = Perro()
gato1 = Gato()

#LLAMANDO hacer_sonido en cada uno
perro1.hacer_sonido()
print("")
gato1.hacer_sonido()