# Escriba aquí su código
def list_min(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] < list_min(lista[1:]):
            return lista[0]
        else:
            return list_min(lista[1:])
