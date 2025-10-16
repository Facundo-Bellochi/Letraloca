from logica import elegir_palabra, verificar_letra, palabra_adivinada
from interfaz import mostrar_estado, pedir_letra, inicializar_palabra, limpiar_pantalla

def main():
    limpiar_pantalla()
    print("Bienvenido al Juego del Ahorcado!")
    input("Presioná ENTER para comenzar...")

    letras_correctas = []
    letras_incorrectas = []
    intentos = 6
    palabra_secreta = elegir_palabra()
    palabra_mostrada = inicializar_palabra(palabra_secreta)

    jugando = True
    ganaste = False

    while jugando:
        limpiar_pantalla()
        mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos)

        letra = pedir_letra()
        resultado = verificar_letra(letra, palabra_secreta, letras_correctas, letras_incorrectas)

        if resultado is True:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        elif resultado is False:
            intentos -= 1
            print(f"¡Mal! La letra '{letra}' no está en la palabra.")
        else:
            print(f"Ya ingresaste la letra '{letra}'. Intentá con otra.")

        # Verificar condiciones de fin
        if palabra_adivinada(palabra_secreta, letras_correctas):
            ganaste = True
            jugando = False
        elif intentos <= 0:
            jugando = False

    limpiar_pantalla()
    mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos)

    if ganaste:
        print("¡Felicidades! ¡Ganaste!")
    else:
        print(f"¡Perdiste! La palabra era '{palabra_secreta}'.")

if __name__ == "__main__":
    main()

#Primero tengo que corregir lo de la interfaz de bienvenida, mostrar menu [Listo]
#Buscar como actualizar la pantalla cada rato para que no tenga que escribir una letra y me salte recien si estaba bien o mal
#Que muestre un mensaje si ganas o si perdes [Listo]
#Crear logica de cuando ganas, hasta ahora solo esta cuando perdes [Listo]
#Mostrar el pj que se actualize si erras y blabla. [Listo]

