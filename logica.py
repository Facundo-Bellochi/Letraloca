import random

def elegir_palabra():
    # Devuelve una palabra aleatoria de la lista
    palabras = [
        "perro","gato","mesa","silla","reloj","queso","playa","lluvia","bosque",
        "tiburon","montania","castillo","barril","nieve","fuego","globo","lapiz",
        "camino","puente","coche","avion","barco","trenes","planeta","jirafa",
        "sombrero","estrella","volcan","ventana","escuela"
    ]
    return random.choice(palabras)

def verificar_letra(letra, palabra, letras_correctas, letras_incorrectas):
    if letra in palabra and letra not in letras_correctas:
        letras_correctas.append(letra)
        return True
    else:
        if letra not in letras_incorrectas:
            letras_incorrectas.append(letra)
        return False

def palabra_adivinada(palabra, letras_correctas):
    # Devuelve True si todas las letras de la palabra están en letras_correctas 
    for letra in palabra:
        if letra not in letras_correctas:
            return False
    return True


# 




