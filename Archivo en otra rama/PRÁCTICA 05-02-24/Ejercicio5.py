import random

def generarNumero():
    return random.randint(0,100)

def preguntaUsuario():
    numeroAAdivinar = generarNumero()
    intentos = 10
    respuestaEstado = False

    print("ADIVINE EL NUMERO DEL 0 AL 100")

    while terminarJuego(intentos, respuestaEstado) == False:
        print("=============================")
        print(f"Tiene {intentos} intentos...")
        numeroUsuario = int(input("Adivine el numero: "))
        respuestaEstado = indicarMayorOMenor(numeroUsuario, numeroAAdivinar)
        intentos = contarIntentos(intentos)
    
    if respuestaEstado == False:
        print("Ya no le quedan intentos :(")
        print(f"La respuesta era {numeroAAdivinar}")

def indicarMayorOMenor(numeroUsuario, numeroAAdivinar):
    if numeroUsuario == numeroAAdivinar:
        print("Respuesta correcta!")
        print("GRACIAS POR JUGAR")
        return True
    elif numeroUsuario < numeroAAdivinar:
        print("El numero es mayor")
        return False
    elif numeroUsuario > numeroAAdivinar:
        print("El numero es menor")
        return False

def contarIntentos(intentos):
    return intentos - 1

def terminarJuego(intentos, respuesta):
    if intentos == 0 or respuesta == True:
        return True
    else:
        return False

preguntaUsuario()