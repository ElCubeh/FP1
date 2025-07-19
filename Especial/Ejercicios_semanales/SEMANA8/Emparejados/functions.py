# Escriba aquí su código
def emparejados(c1, c2, c3):
    elementos = set()
    for elemento in c2:
        if elemento in c1 or elemento in c3:
            elementos.add(elemento)
    for elemento in c3:
        if elemento in c1 or elemento in c2:
            elementos.add(elemento)
    return elementos
