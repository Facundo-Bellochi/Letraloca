import os 

def mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos):
    # Aca mostramos el estado actual del juego
    print("Juego del ahorcado")
    print(f"Errores: {intentos} / 6")
    print("Palabra:", " ".join([letra if letra in letras_correctas else "  " for letra in palabra_secreta]))
    print("Letras incorrectas:", ", ".join(letras_incorrectas))
    print("_" * 30)

def pedir_entrada():
    while True:
        entrada = input("Ingresá una letra o arriesgá la palabra completa: ").lower().strip()
        if not entrada:
            print("No ingresaste nada. Intentá de nuevo.")
            continue
        if len(entrada) == 1 and entrada.isalpha():
            return entrada
        elif len(entrada) > 1 and entrada.isalpha():
            return entrada
        else:
            print("Por favor, ingresá una sola letra válida o una palabra completa.")
# Cambiamos la funcion pedir_letra por pedir_entrada para que se entienda que cambiamos la funcion completa



def inicializar_palabra(palabra):
    # Aca hacemos la lista de guiones para la palabra
    return [""] * len(palabra)

def limpiar_pantalla():
    # Limpia la pantalla de la consola
    os.system('cls' if os.name == 'nt' else 'clear')