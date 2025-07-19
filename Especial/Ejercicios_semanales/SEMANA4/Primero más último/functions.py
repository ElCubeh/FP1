# Escriba su código aquí
def first_plus_last(my_tuple):
    if not my_tuple:
        return 0
    first_element = my_tuple[0]
    last_element = my_tuple[-1]
    return first_element + last_element
    