import random
from interfaz import limpiar_pantalla, mostrar_estado, pedir_entrada, bienvenida



# Constantes global: lista de palabras disponibles y maximo de intentos.
PALABRAS = [
    "perro","gato","mesa","silla","reloj","queso","playa","lluvia","bosque",
    "tiburon","montania","castillo","barril","nieve","fuego","globo","lapiz",
    "camino","puente","coche","avion","barco","trenes","planeta","jirafa",
    "sombrero","estrella","volcan","ventana","escuela"
]
MAX_INTENTOS = 6 


def elegir_palabra():
    return random.choice(PALABRAS)


def verificar_letra(letra, palabra, letras_correctas, letras_incorrectas):
    es_correcta = letra in palabra 
    if es_correcta:
        letras_correctas.append(letra)
    else:
       letras_incorrectas.append(letra)
    return es_correcta

def palabra_adivinada(palabra, letras_correctas):
    todas_adivinadas = True
    for letra in palabra:
        if letra not in letras_correctas:
            todas_adivinadas = False
    return todas_adivinadas


def jugar_ahorcado():
    limpiar_pantalla()
    bienvenida()
    intentos = MAX_INTENTOS
    letras_correctas = []
    letras_incorrectas = []
    
    palabra_secreta = elegir_palabra()

    jugando = True
    ganaste = False

    while jugando:
        mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos)
        entrada = pedir_entrada() 

        if len(entrada) == 1:
            letra = entrada
            if letra in letras_correctas or letra in letras_incorrectas:
                print(f"Ya ingresaste la letra '{letra}'. Intentá con otra.")
                continue 

            resultado = verificar_letra(letra, palabra_secreta, letras_correctas, letras_incorrectas)

            if resultado is True:
                print(f"¡Bien! La letra '{letra}' está en la palabra.")
            elif resultado is False:
                intentos -= 1
                print(f"¡Mal! La letra '{letra}' no está en la palabra.")

        else:
            palabra_arriesgada = entrada
            print(f"Arriesgaste la palabra: '{palabra_arriesgada}'")
            
            if palabra_arriesgada == palabra_secreta:                
                ganaste = True
                jugando = False
                print("¡Arriesgo correcto!")
                
            else:
                intentos -= 1
                print("¡Palabra incorrecta! ¡Has perdido por arriesgar mal!")
                jugando = False 
                ganaste = False

        if not ganaste and palabra_adivinada(palabra_secreta, letras_correctas):
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


