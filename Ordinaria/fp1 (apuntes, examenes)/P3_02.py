# Dada una tupla conteniendo diversos valores, escriba una función, hay_elementos(tupla, tipo), donde tipo es un tipo de datos
# de Python, que devuelva True si la tupla contiene algún elemento del tipo indicado por el segundo parámetro y False si no
# contiene ninguno.

# Incluya en el módulo una sección para ejecutar como "__main__" que cree una tupla con un número entero, una string, una tupla
# con cualquier clase de elementos, y un valor booleano, y muestre en pantalla el resultado de llamar a
# hay_elementos(tupla, tipo), con los tipos int, float, str, tuple y bool, en este orden.

def hay_elementos(tupla, tipo):
    for elemento in tupla:
        if type(elemento) == tipo:
            return True
    return False

if "__main__" == __name__:
    a = (7, "hola", ("feo", 9), True)
    print(hay_elementos(a, int))
    print(hay_elementos(a, float))
    print(hay_elementos(a, str))
    print(hay_elementos(a, tuple))
    print(hay_elementos(a, bool))