# Esciba su código aquí
def min_of_matrix(matriz):
    min_val = float('inf')
    for row in matriz:
        for elem in row:
            min_val = min(min_val, elem)
    return min_val
