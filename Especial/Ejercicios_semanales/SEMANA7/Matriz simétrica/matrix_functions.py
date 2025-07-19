# Escriba aquí su código
def symmetrical(matriz):
    size = len(matriz)
    for i in range(size):
        for j in range(i + 1, size):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
