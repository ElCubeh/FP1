# Escriba aquí la función
def binary_search(data, num):

    if len(data) == 0:
        return False
    
    medio = len(data) // 2
    if num == data[medio]:
        return True
    elif num < data[medio]:
        return binary_search(data[medio + 1:], num)
    else:
        return binary_search(data[:medio], num)




if __name__ == "__main__":
    data = [
        38, 48, 56, 65, 76, 89, 92, 95, 105, 107,
        112, 117, 120, 126, 128, 130, 145, 154
    ]

    for num in range(90, 100):
        found = binary_search(data, num)
        print(f"¿Está el número {num}? {'Sí' if found else 'No'}")