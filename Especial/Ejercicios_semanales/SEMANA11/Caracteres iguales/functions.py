# Escriba su código aquí
def caracteres_iguales(c1, c2):
    if not c1 or not c2:
        return []
    if c1[0] == c2[0]:
        return [1] + caracteres_iguales(c1[1:], c2[1:])
    else:
        return [0] + caracteres_iguales(c1[1:], c2[1:])
