# Escriba aquí su código
def count_values(list1, list2):
    count_dict = {}
    for num in list1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for i in range(len(list2)):
        num = list2[i]
        list2[i] = (num, count_dict.get(num, 0))
    return list2
