# Escriba aquí su código
def sumar_multiplos(lista1, lista2, m):
    suma = 0
    for i in range(len(lista1)):
        if (lista1[i] + lista2[i]) % m == 0:
            suma += lista1[i] + lista2[i]
    return suma
