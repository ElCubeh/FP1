# Escriba aquí su código
def valores_en_rango(lista, range_inf, range_sup):
    result = set()
    for elemento in lista:
        if range_inf <= elemento <= range_sup:
            result.add(elemento)
    return result
