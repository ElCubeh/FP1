# Escriba una función tipos(elementos) que, siendo elementos una lista conteniendo valores que pueden ser de diferentes tipos,
# devuelva una lista del mismo tamaño que el de elementos, de forma que cada elemento de la lista devuelta sea una string cuyo
# valor sea el nombre del tipo del elemento que ocupa la misma posición en la lista elementos.

# Ejemplo de uso de la función tipos:

# mi_dato = mi_tipo()
# elementos = [1, "Hola", 3.14, True, [1, 2, 3], mi_dato]
# tipos_elementos = tipos(elementos)
# print(tipos_elementos)  # Muestra ['int', 'str', 'float', 'bool', 'list', 'mi_tipo']

def tipos(lista):
    res = []
    for elemento in lista:
        res.append(type(elemento).__name__) #Para quitar "<class __>" del resultado al imprimirlo
    return res

if __name__ == "__main__":
    elementos = [1, "Hola", 3.14, True, [1, 2, 3]]
    tipos_elementos = tipos(elementos)
    print(tipos_elementos)  # ['int', 'str', 'float', 'bool', 'list']