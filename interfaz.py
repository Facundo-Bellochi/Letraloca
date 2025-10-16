def mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos):
    print("Juego del ahorcado")
    print(f"Errores: {intentos} / 6")
    print("Palabra:", " ".join([letra if letra in letras_correctas else "  " for letra in palabra_secreta]))
    print("Letras incorrectas:", ", ".join(letras_incorrectas))

def pedir_letra():
    letra = input("Ingresá una letra: ").lower()
    while not letra.isalpha() or len(letra) != 1:
        letra = input("Por favor, ingresá una sola letra válida: ").lower()
    return letra
def inicializarpalabra(palabra):
    return [""] * len(palabra)
