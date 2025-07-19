# Escriba aquí la función
def binary_search(sorted_sequence, value):
    if len(sorted_sequence) == 0:
        return False
    mid = len(sorted_sequence) // 2
    if sorted_sequence[mid] == value:
        return True
    elif sorted_sequence[mid] > value:
        return binary_search(sorted_sequence[:mid], value)
    else:
        return binary_search(sorted_sequence[mid+1:], value)


if __name__ == "__main__":
    data = [
        38, 48, 56, 65, 76, 89, 92, 95, 105, 107,
        112, 117, 120, 126, 128, 130, 145, 154
    ]

    for num in range(90, 100):
        found = binary_search(data, num)
        print(f"¿Está el número {num}? {'Sí' if found else 'No'}")
