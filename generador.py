from typing import List
from random import shuffle

def generadorDeAldeanos(nombres: List, apellidos: List) -> str:
    shuffle(nombres)    # Mezcla aleatoriamente los nombres
    shuffle(apellidos)  # Mezcla aleatoriamente los apellidos

    while len(nombres) and len(apellidos):
        yield f"{nombres.pop()} {apellidos.pop()}"

    yield "NO QUEDA NADIE EN LA ALDEA"


if __name__ == "__main__":
    aldea = generadorDeAldeanos(
        ["Paco", "Marta", "Lucía", "Lucía"],
        ["Ortíz", "González", "Pescadero", "Pérez", "Castillos"]
    )

    print(next(aldea))
    print(next(aldea))
    print(next(aldea))
    print(next(aldea))
    # Esto imprimirá "NO QUEDA NADIE EN LA ALDEA"
    print(next(aldea))

    # Si haces más `next(aldea)` dará StopIteration
