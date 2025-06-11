# juego de bola magica que coge las frases del archivo frases.txt
import random

FILENAME = "frases.txt"

def mostrar_respuesta(respuestas):
    print(random.choice(respuestas))

def cargar_respuestas(nombre_archivo):
    try:
        manejador_de_fichero = open(nombre_archivo)
    except FileNotFoundError:
        print("Error archivo no encontrado")
        return []
    except FileExistsError:
        print("Error archivo no existe")
        return []
    except PermissionError:
        print("no tienes permisos para este archivo")
        return []
    
    respuestas = []
    for linea in manejador_de_fichero:
        respuestas.append(linea)
    manejador_de_fichero.close()
    return respuestas

if __name__ == "__main__": 
    respuestas = cargar_respuestas(FILENAME)
    if respuestas:
        mostrar_respuesta(respuestas)