# Escriba su código aquí
def division(a, b):
    if b == 0:
        return 'No se puede dividir por 0'
    cociente = a // b
    resto = a % b
    return {'Cociente': cociente, 'Resto': resto}
