# Escriba su código aquí
def square_root(number, accuracy):
    result = number
    while abs(result - number / result) > accuracy / 2:
        result = (number / result + result) / 2
    return result