# Escriba su código aquí
def product(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + product(a, b-1)
    if b < 0:
        return -product(a, -b)
