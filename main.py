import math
from random import randint

a = None

try:
    aleat = randint(0, 2)
    if aleat == 0:
        a = math.exp(1000)
    elif aleat == 1:
        a = 3 / 0
    else:
        raise FloatingPointError("Operación de punto flotante inválida")

except ZeroDivisionError as e:
    a = 9999
except OverflowError as e:
    a = 1000
except ArithmeticError as e:
    print("ERROR MATEMATICO DESCONOCIDO")
    a = "INVALIDO"
except Exception as:


print(f"RESULTADO {a}")
















# TypeError: 'float' object cannot be interpreted as an integer
"""
for i in range(0.1):
    pass
"""