# Escriba aquí su código
def is_sym(lst):
    if not lst:
        return True
    elif len(lst) == 1:
        return True
    else:
        return lst[0] == lst[-1] and is_sym(lst[1:-1])
