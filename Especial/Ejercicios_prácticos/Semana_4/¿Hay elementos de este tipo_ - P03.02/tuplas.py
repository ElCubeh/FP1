def hay_elementos(tupla, tipo):
    for i in tupla:
        if type(i) is tipo:
            return True
    return False


if __name__ == "__main__":

    tupla = (69, "Hello World!", (True, 6), False)
    tipo = int
    print(hay_elementos(tupla, tipo))
