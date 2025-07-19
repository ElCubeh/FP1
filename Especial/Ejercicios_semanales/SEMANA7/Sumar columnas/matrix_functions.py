# Escriba aquí su código
def sum_columns(matriz):
    if not matriz:
        return []
    columns = len(matriz[0])
    columns_sums = [0] * columns
    for row in matriz:
        for i in range(columns):
            columns_sums[i] += row[i]
    return columns_sums
