# Escriba su código aquí
def divisibles(lista, num):
    cuenta = 0
    for i in lista:
        if i % num == 0:
            cuenta += 1
    return cuenta
