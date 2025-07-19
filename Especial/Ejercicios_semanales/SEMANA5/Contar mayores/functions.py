# Escriba su código aquí
def contar_mayores(tupla, valor):
    contador = 0
    for elemento in tupla:
        if elemento > valor:
            contador += 1
    return contador