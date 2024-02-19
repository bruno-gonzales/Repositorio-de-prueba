#1. Crea una clase base Vehículo con atributos comunes como marca y modelo y un método mostrar_detlle
#2. Crea dos clases que hereden de Vehículo: Coche y Bicicleta.
#3. Coche tiene un atributo adicional caballos_de_fuerza y sobrescribe el método mostrar_detalle para incluir este nuevo atributo.
#4. Bicicleta tiene un atributo adiciona tipo (puede ser "urbana", "montaña", etc.) y también sobrescribe el método mostrar_detalle.
#Demuestra como se pueden crear instancias de Coche y Bicicleta y cómo llamar a sus métodos

class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_detalle(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}", end=", ")

class Coche(Vehículo):
    def __init__(self, marca, modelo, caballos_de_fuerza):
        super().__init__(marca, modelo)
        self.caballos_de_fuerza = caballos_de_fuerza
    
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Caballos de fuerza: {self.caballos_de_fuerza}")

class Bicicleta(Vehículo):
    def __init__(self, marca, modelo, tipo_bici):
        super().__init__(marca, modelo)
        self.tipo_bici = tipo_bici
    
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Tipo de bicicleta: {self.tipo_bici}")

#CREANDO OBBJETOS O INSTANCIAS
vehículo1 = Vehículo("Hyundai", "Elantra")
coche1 = Coche("Toyota", "Corolla", "133CV")
bicicleta1 = Bicicleta("MONARK", "Huffy", "De montaña")

#LLAMANDO AL MÉTODO mostrar_detlle
vehículos = [vehículo1, coche1, bicicleta1]
for vehículo in vehículos:
    vehículo.mostrar_detalle()