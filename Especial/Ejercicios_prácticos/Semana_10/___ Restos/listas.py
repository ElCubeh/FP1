# Escriba aquí su código
def restos(l1, l2):
    resultado = []
    if l1 == 0:
        return resultado.append(l1)
    elif l2 == 0:
        return resultado.append(l2)
    else:
        for i, j in zip(l1, l2):
            if i >= j:
                resultado.append(i % j)
            elif i <= j:
                resultado.append(-1)
    return resultado


if __name__ == "__main__":
    list1 = [1, 3, 5, 9, 2, 8, 7]
    list2 = [8, 4, 2, 6, 5, 7, 3, 9]
    resultado = restos(list1, list2)
    print(resultado)
