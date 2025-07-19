def suma(tupla):
    total = 0
    for i in tupla:
        total += i
    return total


if __name__ == "__main__":
    tupla = (5, 10, 2, 8, 3)
    print(suma(tupla))
