# Escriba aquí la función
def restos(lista1, lista2):
    lista = []
    for a, b in zip(lista1, lista2):
        if a > b:
            lista.append(a % b)
        else:
            lista.append(b % a)
    return lista


if __name__ == "__main__":
    lista1 = [8, 12, 5, 10]
    lista2 = [3, 4, 2, 5]
    restos_lista = restos(lista1, lista2)
    print(restos_lista)
