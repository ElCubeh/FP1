def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 != 0:
            return True
    elif año % 400 == 0:
        return True
    return False