# Escriba su código aquí
def no_decreasing(lista):
    if len(lista) == 0:
        return True
    elif len(lista) == 1:
        return True
    else:
        for i in range(1, len(lista)):
            if lista[i] < lista[i-1]:
                return False
        return True
