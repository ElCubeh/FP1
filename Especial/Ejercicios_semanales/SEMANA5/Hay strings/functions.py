# Escriba su código aquí
def contains_strs(tupla):
    for element in tupla:
        if isinstance(element, str):
            contains_strs = True
            break
    return contains_strs
