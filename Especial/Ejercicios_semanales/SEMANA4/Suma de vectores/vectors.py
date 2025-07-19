# Escriba su código aquí
def vector_sum(vector1, vector2):
    suma = list()
    if len(vector1) == len(vector2):
        for i in range(0,len(vector1)):
            suma.append(vector1[i]+vector2[i])
    return tuple(suma)
    