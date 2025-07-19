# Escriba su código aquí
def smallest(lista):
    altura_min = lista[0]
    indice_min = 0
    for i in range(1, len(lista)):
        if lista[i] < altura_min:
            altura_min = lista[i]
            indice_min = i
    return (altura_min, indice_min)
