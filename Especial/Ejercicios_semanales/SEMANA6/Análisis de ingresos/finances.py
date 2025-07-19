# Escriba aquí su código
def best_semester(income_list):
    if not isinstance(income_list, list) or len(income_list) != 12:
        return None
    total_income = sum(income_list)
    semester1 = sum(income_list[:6])
    semester2 = total_income - semester1
    if semester1 > semester2:
        return 1
    elif semester1 < semester2:
        return 2
    else:
        return 0
