# Escriba aquí su código
def join_lists(list1, list2):
    min_len = min(len(list1), len(list2))
    return {list1[i]: list2[i] for i in range(min_len)}
