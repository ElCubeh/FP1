# Escriba aquí su código
def load_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    list_of_lists = []
    for line in lines:
        line = line.strip()
        str_list = line.split()
        int_list = [int(str_num) for str_num in str_list]
        list_of_lists.append(int_list)
    return list_of_lists
