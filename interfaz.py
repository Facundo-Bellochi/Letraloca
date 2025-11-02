import os 

def pedir_respuesta_continuar():
    return input("\n¿Querés jugar de nuevo? (S/N): ").lower().strip()

def mostrar_mensaje_error_continuar():
    print("⚠️ Error: Opción no válida. Por favor, ingresá 'S' (Sí) o 'N' (No).")

def mostrar_mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Hasta pronto!")

def mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos):
    # Aca mostramos el estado actual del juego
    print("Juego del ahorcado")
    print(f"Errores: {intentos} / 6")
    print("Palabra:", " ".join([letra if letra in letras_correctas else "_" for letra in palabra_secreta]))
    print("Letras incorrectas:", ", ".join(letras_incorrectas))
    print("_" * 30)

def pedir_entrada():
    while True:
        entrada = input("Ingresá una letra o arriesgá la palabra completa: ").lower().strip()
        if not entrada:
            print("No ingresaste nada. Intentá de nuevo.")
            continue
        if entrada.isalpha(): 
            return entrada
        else:
            print("Por favor, ingresá solo letras.")        

def limpiar_pantalla():   
    os.system('cls' if os.name == 'nt' else 'clear')