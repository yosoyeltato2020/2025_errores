monstruos = 3
exp = 0

def experiencia(accion):
    def aaa():
        global exp
        resultado = accion()
        exp += 1
        return resultado
    return aaa

def matar():
    global monstruos
    monstruos -= 1

print(f"quedan {monstruos} monstruos")
matar()
