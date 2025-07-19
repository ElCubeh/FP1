# Escriba aquí su código
def delete_value(num_list, value):
    while value in num_list:
        num_list.remove(value)
    return num_list
