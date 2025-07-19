# Escriba aquí su código
def filter_names(name_list, filter_num):
    filtered_names = []
    if filter_num % 2 == 0:
        for i in range(0, len(name_list), 2):
            filtered_names.append(name_list[i])
    else:
        for i in range(1, len(name_list), 2):
            filtered_names.append(name_list[i])
    return filtered_names
