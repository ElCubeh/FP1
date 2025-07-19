# Escriba aquí su código
def initials(lista):
    result = []
    for sub_lista in lista:
        new_sub_lista = []
        for name in sub_lista:
            initial = name[0]
            new_sub_lista.append(initial)
        result.append(new_sub_lista)
    return result
