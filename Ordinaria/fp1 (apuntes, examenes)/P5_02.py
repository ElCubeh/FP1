# Escriba una función restos(lista1, lista2) que tome como parámetros dos listas de números mayores que cero.
# La función deberá devolver una nueva lista cuyo tamaño sea igual al menor de los tamaños de las listas recibidas
# como parámetros. Cada posición de la nueva lista contendrá el resto de dividir el mayor por el menor de los elementos
# que ocupen esa misma posición en lista1 y lista2.

# Ejemplo:

# lista1 = [8, 12, 2, 10]
# lista2 = [3, 4, 5, 5]
# restos_lista = restos(lista1, lista2)
# print(restos_lista) ==> muestra [2, 0, 1, 0]

def restos(l1, l2):
    res = []

    mini = min(len(l1), len(l2))

    for i in range(mini):
        if l1[i] > l2[i]:
            res.append(l1[i]%l2[i])
        else:
            res.append(l2[i]%l1[i])
    return res

if __name__ == "__main__":
    lista1 = [8, 12, 5, 10, 0]
    lista2 = [3, 4, 2, 5]
    restos_lista = restos(lista1, lista2)
    print(restos_lista)