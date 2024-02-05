#CONDICIONAL

if 5 > 3:
    print("5 es mayor que 3")
else:
    print("5 no es mayor que 3")

#CONDICIONAL ANIDADO

if 5 > 3:
    print("5 es mayor que 3")
elif 5 == 3:
    print("5 es igual que 3")
else:
    print("5 no es mayor que 3")

monto = 5000

if monto > 3000:
    descuento = monto * 0.2
elif monto > 1000:
    descuento = monto * 0.1
else:
    descuento = 0

print("Su descuento es ", descuento)

#LECTURA DE DATOS CON EL TECLADO

sueldoEmpleado = float(input("Ingrese el sueldo del empleado: S./ "))

descuentoAfp = sueldoEmpleado * 0.1
descuentoSeguro = sueldoEmpleado * 0.05

if 0 < sueldoEmpleado <= 1025:
    descuentoAfp = 0
    descuentoSeguro = 0
    bono = sueldoEmpleado * 0.1
elif 1025 < sueldoEmpleado <= 1500:
    bono = sueldoEmpleado * 0.5
elif 1500 < sueldoEmpleado <= 2000:
    bono = 0
else:
    print("El sueldo ingresado no es válido")

descuentoEmpleado = descuentoAfp + descuentoSeguro

sueldoNetoEmple = sueldoEmpleado - descuentoEmpleado + bono

#EJEMPLO DE CAJERO
montoCajero = 500

print("Bienvenido al cajero!")
print("1. Consultar saldo")
print("2. ")