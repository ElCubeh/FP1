# Escriba aquí su código
def maxs(list1, list2):
    max_list = []
    max_length = max(len(list1), len(list2))
    for i in range(max_length):
        max_val = -1
        if i < len(list1):
            max_val = max(max_val, list1[i])
        if i < len(list2):
            max_val = max(max_val, list2[i])
        max_list.append(max_val)
    return max_list
