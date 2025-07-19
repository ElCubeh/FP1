# Escriba aquí su código
def count_values(num_list1, num_list2):
    count_dict = {}
    for num in num_list1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    count_list = []
    for num in num_list2:
        if num in count_dict:
            count_list.append(count_dict[num])
        else:
            count_list.append(0)
    return count_list
