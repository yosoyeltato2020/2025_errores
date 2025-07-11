# juego de bola magica que coge las frases del archivo frases.txt
import random

FILENAME = "frases.txt"

def mostrar_respuesta(respuestas):
    print(random.choice(respuestas))

def cargar_respuestas(respuestas):
    try:
        manejador_de_fichero = open("frases.txt")
    except FileNotFoundError:
        print("Error archivo no encontrado")
    except FileExistsError:
        print("Error archivo no exite")
    except PermissionError:
        print("no tienes permisos para este archivo")
    
    respuestas = []
    for linea in manejador_de_fichero:
        respuestas.append(linea)

    manejador_de_fichero.close()

    return respuestas

if __name__ == "__main__": 
    respuestas = cargar_respuestas(FILENAME)
    mostrar_respuesta(respuestas)
