#Explora la herencia múltiple y el uso de super():

#1. Crea una clase base Forma con un método dibujar() que simplemente imprime "Dibujando forma".
#2. Crea otra clase base Color con un método pintar() que imprime "Pintando con [color]" donde [color] es un atributo de la clase.
#3. Crea una clase CuadradoColorido que herede de ambas clases, Forma y Color, y utiliza super() para llamar a los métodos de las clases padres de manera adecuada para demostrar cómo se puede trabajar con herencia múltiple.

#CRENADO CLASE FORMA CON METODO DIBUJJA
class Forma():
    def dibujar(self):
        print("Dibujando forma...")

#CREANDO CLASE COLOR CON SU METODO Y ATRIBUTO
class Color:
    def __init__(self, color):
        self.color = color
    
    def pintar(self):
        print(f"Pintando con {self.color}...")

#CREANDO CLASE CUADRADO COLORIDO Y USANDO super(). PARA CADA METODO
class CuadradoColorido (Forma, Color):
    def __init__(self, color):
        Forma.__init__(self)
        super().__init__(color)

    def dibujar(self):
        super().dibujar()
    
    def pintar(self):
        super().pintar()

#CREANDO INSTANCIA
cuadrado1 = CuadradoColorido("azul")

#LLAMANDO LOS METODOS
cuadrado1.dibujar()
cuadrado1.pintar()