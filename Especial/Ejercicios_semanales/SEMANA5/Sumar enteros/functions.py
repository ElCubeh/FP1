# Escriba su código aquí
def sum_ints(t):
    sum = 0
    for element in t:
        if isinstance(element, int):
            sum += element
    return sum