import os 
def bienvenida():
    print("Bienvenido al Juego del Ahorcado!")
    input("Presioná ENTER para comenzar...")

def pedir_respuesta_continuar():
    return input("\n¿Querés jugar de nuevo? (S/N): ").lower().strip()

def mostrar_mensaje_error_continuar():
    print("⚠️ Error: Opción no válida. Por favor, ingresá 'S' (Sí) o 'N' (No).")

def mostrar_mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Hasta pronto!")

def mostrar_estado(palabra_secreta, letras_correctas, letras_incorrectas, intentos):
    # Aca mostramos el estado actual del juego
    estado_palabra = " ".join([letra if letra in letras_correctas else "_" for letra in palabra_secreta])
    texto_izq = (
        "Juego del ahorcado\n"
        f"Errores: {intentos} / 6\n"
        f"Palabra: {estado_palabra}\n"
        f"Letras incorrectas: {', '.join(letras_incorrectas) if letras_incorrectas else 'Ninguna'}\n"
        + "_" * 30
    )
    dibujo = obtener_dibujo(intentos)
    imprimir_dos_columnas(texto_izq, dibujo)

def obtener_dibujo(intentos):
    dibujos = [
        # 0 errores
        """ 
    +---+
        |

        
        
    =========
""",
        # 1 error
        """ 
    +---+
        |
        O
        
        
    =========
""",
        # 2 errores
        """ 
    +---+
    |   |
        O
        |
        
    =========
""",
        # 3 errores
        """ 
    +---+
    |   |
    |   O
       /|
        
    =========
""",
        # 4 errores
        """ 
    +---+
    |   |
    |   O
    |  /|\\
        
    =========
""",
        # 5 errores
        """ 
    +---+
    |   |
    |   O
    |  /|\\
       /
    =========
""",
        # 6 errores
        """ 
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    =========
"""
    ]
    # Limitar a 6 errores
    return dibujos[min(intentos, 6)]

def imprimir_dos_columnas(texto_izq, dibujo_der):
    izq = texto_izq.split("\n")
    der = dibujo_der.split("\n")

    max_lineas = max(len(izq), len(der))

    for i in range(max_lineas):
        col_izq = izq[i] if i < len(izq) else ""
        col_der = der[i] if i < len(der) else ""
        print(f"{col_izq:<35} {col_der}")  # 35 = ancho columna izquierda


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