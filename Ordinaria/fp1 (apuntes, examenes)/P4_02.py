# Escriba una función suma(tupla) que, siendo el parámetro una tupla de enteros, devuelva sin usar la función sum() de Python
# el valor resultante de sumar todos los elementos de la tupla.

# Incluya en el módulo una sección a ejecutar como "__main__" que cree una tupla con los valores 5, 10, 2, 8 y 3; usándola
# a continuación para llamar a la función y mostrar su resultado en pantalla.

def suma(tupla):
    resultado = 0
    for element in tupla:
        resultado += element
    return resultado


if __name__ == "__main__":
    tup = (5, 10, 2, 8, 3)
    print(suma(tup))
