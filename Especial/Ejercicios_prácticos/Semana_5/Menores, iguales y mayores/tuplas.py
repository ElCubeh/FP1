def menores_o_iguales(tuplas, numero):
    menores = 0
    iguales = 0
    mayores = 0
    for i in tuplas:
        if i < numero:
            menores += 1
        elif i == numero:
            iguales += 1
        elif i > numero:
            mayores += 1

    return (menores, iguales, mayores)


if __name__ == "__main__":

    tupla = (2, 5, 1, 3, 2, 5, 6, 3, 2, 1)
    numero = 3
    resultado = menores_o_iguales(tupla, numero)
    print(resultado)
