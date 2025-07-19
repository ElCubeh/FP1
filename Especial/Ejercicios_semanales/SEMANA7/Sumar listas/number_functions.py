# Escriba aquí su código
def sum_lists(list1, list2):
    length = max(len(list1), len(list2))
    sum_list = []
    for i in range(length):
        if i >= len(list1):
            list1_element = 0
        else:
            list1_element = list1[i]
        if i >= len(list2):
            list2_element = 0
        else:
            list2_element = list2[i]
        sum_list.append(list1_element + list2_element)
    return sum_list
