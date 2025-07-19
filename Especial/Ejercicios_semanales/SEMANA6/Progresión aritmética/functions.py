# Escriba su código aquí
def progresion(valor1, diff, n):
    if n < 1:
        return[]
    lista = [valor1]
    for i in range(1, n):
        lista.append(lista[-1] + diff)
    return lista
