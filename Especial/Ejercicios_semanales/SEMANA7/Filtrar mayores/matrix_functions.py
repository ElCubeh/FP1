# Escriba aquí su código
def pass_highers(matriz, numero):
    matriz_new = []
    for row in matriz:
        new_row = [n for n in row if n >= numero]
        matriz_new.append(new_row)
    return matriz_new
