# Escriba su código aquí
def avg_grade(grade_list):
    try:
        avg = sum(grade_list) / len(grade_list)
        return round(avg, 2)
    except ZeroDivisionError:
        return None
    except TypeError:
        return None
