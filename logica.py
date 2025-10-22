import random
from interfaz import limpiar_pantalla, inicializar_palabra, mostrar_estado, pedir_entrada



# Constante global: lista de palabras disponibles
PALABRAS = [
    "perro","gato","mesa","silla","reloj","queso","playa","lluvia","bosque",
    "tiburon","montania","castillo","barril","nieve","fuego","globo","lapiz",
    "camino","puente","coche","avion","barco","trenes","planeta","jirafa",
    "sombrero","estrella","volcan","ventana","escuela"
]

def elegir_palabra():
    return random.choice(PALABRAS)
# Transformamos la funcion anterior en una constante llamada a funcion como pidio el profesor +

def verificar_letra(letra, palabra, letras_correctas, letras_incorrectas):
    correcta = letra in palabra

    if correcta and letra not in letras_correctas:
        letras_correctas.append(letra)
    elif not correcta and letra not in letras_incorrectas:
        letras_incorrectas.append(letra)

    return correcta
# Cambiamos el doble return a uno solo, dando correcta al terminar.

def palabra_adivinada(palabra, letras_correctas):
    todas_adivinadas = True
    for letra in palabra:
        if letra not in letras_correctas:
            todas_adivinadas = False
    return todas_adivinadas
# le sacamos los dos returns
# usamos una palabra inicializada en true para transformar 2 returns en 1






def jugar_ahorcado():
    limpiar_pantalla()
    print("Bienvenido al Juego del Ahorcado!")
    input("Presioná ENTER para comenzar...")

    letras_correctas = []
    letras_incorrectas = []
    intentos = 6
    palabra_secreta = elegir_palabra()
    palabra_mostrada = inicializar_palabra(palabra_secreta) # Esta línea no es estrictamente necesaria aquí, pero la dejo.

    jugando = True
    ganaste = False

    while jugando:
        limpiar_pantalla()
        mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos)

        # Usar la función renombrada
        entrada = pedir_entrada() 

        if len(entrada) == 1:
            # Lógica para adivinar una letra
            letra = entrada
            # **Añadir verificación de letra ya intentada (faltante en tu código original)**
            if letra in letras_correctas or letra in letras_incorrectas:
                print(f"Ya ingresaste la letra '{letra}'. Intentá con otra.")
                # Usa 'continue' para volver al inicio del bucle sin perder un intento
                continue 

            resultado = verificar_letra(letra, palabra_secreta, letras_correctas, letras_incorrectas)

            if resultado is True:
                print(f"¡Bien! La letra '{letra}' está en la palabra.")
            elif resultado is False:
                intentos -= 1
                print(f"¡Mal! La letra '{letra}' no está en la palabra.")
            # La condición 'else' del código original ya no es necesaria si verificamos antes.
            # else:
            #     print(f"Ya ingresaste la letra '{letra}'. Intentá con otra.")

        else:
            # Lógica para arriesgar una palabra
            palabra_arriesgada = entrada
            print(f"Arriesgaste la palabra: '{palabra_arriesgada}'")
            
            if palabra_arriesgada == palabra_secreta:
                # Si acierta, considera todas las letras como correctas para el display final
                for letra in palabra_secreta:
                    if letra not in letras_correctas:
                        letras_correctas.append(letra)
                ganaste = True
                jugando = False
                print("¡Arriesgo correcto!")
            else:
                intentos -= 1
                print("¡Palabra incorrecta! Perdés un intento.")


        # Verificar condiciones de fin
        if not ganaste and palabra_adivinada(palabra_secreta, letras_correctas):
            ganaste = True
            jugando = False
        elif intentos <= 0:
            jugando = False
            
    # ... (El resto de la función es igual)
    limpiar_pantalla()
    mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos)

    if ganaste:
        print("¡Felicidades! ¡Ganaste!")
    else:
        print(f"¡Perdiste! La palabra era '{palabra_secreta}'.")


