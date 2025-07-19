# Escriba aquí la función solicitada
def cuantos_hay(tupla, tipo):
    count = 0
    for i in tupla:
        if type(i) is tipo:
            count += 1
    return count


if __name__ == "__main__":
    tupla = (1, 'Hola', (1, 2, 3), True, 'Hola')

    print(cuantos_hay(tupla, int))    # 1
    print(cuantos_hay(tupla, str))    # 2
    print(cuantos_hay(tupla, tuple))  # 1
    print(cuantos_hay(tupla, bool))   # 1
    print(cuantos_hay(tupla, float))  # 0
