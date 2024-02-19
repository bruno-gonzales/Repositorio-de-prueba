class Vehículo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def mostrar_detalle(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")

class Coche(Vehículo):
    def __init__(self, marca, modelo, color, cilindraje):
        super().__init__(marca, modelo, color)
        self.cilindraje = cilindraje
    
    def mostrar_detalle(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Cilindraje: {self.cilindraje}")

class Moto(Vehículo):
    def __init__(self, marca, modelo, color, tipo_moto):
        super().__init__(marca, modelo, color)
        self.tipo_moto = tipo_moto
    
    def mostrar_detalle(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Tipo de moto: {self.tipo_moto}")

#CREANDO OBBJETOS O INSTANCIAS
vehículo1 = Vehículo("Nissan", "Versa", "Blanco")
coche1 = Coche("Toyota", "Prado", "Blanco", 1600)
moto1 = Moto("Honda", "CBR", "Rojo", "Deportiva")

#LLAMANDO AL MÉTODO mostrar_detlle
vehículos = [vehículo1, coche1, moto1]
for vehículo in vehículos:
    vehículo.mostrar_detalle()