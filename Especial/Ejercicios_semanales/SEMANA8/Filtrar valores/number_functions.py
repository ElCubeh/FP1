# Escriba aquí su código
def filter_values(dict_pares, min_val, max_val):
    result = {}
    for key, value in dict_pares.items():
        if min_val <= value <= max_val:
            result[key] = value
    return result
