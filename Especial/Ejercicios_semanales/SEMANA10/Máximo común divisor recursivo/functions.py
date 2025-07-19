# Escriba su código aquí
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
