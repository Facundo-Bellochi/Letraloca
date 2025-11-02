from logica import jugar_ahorcado
from interfaz import limpiar_pantalla, pedir_respuesta_continuar, mostrar_mensaje_error_continuar, mostrar_mensaje_despedida

def main():
    jugar_otra_vez = True 
    while jugar_otra_vez:
        
        limpiar_pantalla()
        jugar_ahorcado()

        respuesta_valida = False
        while not respuesta_valida:
            respuesta = pedir_respuesta_continuar() 
            if respuesta in ('s', 'si', 'Si', 'Yes', 'yes'):
                respuesta_valida = True
            elif respuesta in ('n', 'no', 'No'):
                mostrar_mensaje_despedida() 
                jugar_otra_vez = False  
                respuesta_valida = True 
            else:
                mostrar_mensaje_error_continuar()
            
if __name__ == "__main__":
    main()