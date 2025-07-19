# Escriba su código aquí
def mcd(a, b):
    if a < b:
        return mcd(b, a)
    if b == 0:
        return a
    r = a % b
    return mcd(b, r)