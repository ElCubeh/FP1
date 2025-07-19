# Escriba aquí la función
def tipos(elementos):
    r = []
    for i in elementos:
        r.append(type(i).__name__)
    return r


if __name__ == "__main__":
    elementos = [1, "Hola", 3.14, True, [1, 2, 3]]
    tipos_elementos = tipos(elementos)
    print(tipos_elementos)  # ['int', 'str', 'float', 'bool', 'list']
