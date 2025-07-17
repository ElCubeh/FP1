# El factorial de un número entero positivo se define como el producto de todos los números enteros comprendidos entre 1 y
# ese número, ambos incluidos; el factorial de 0 es 1; y no existe factorial para los números negativos.

# Escriba en el fichero funciones.py una función factorial(n), donde n es un número entero. La función debe devolver el valor
# del factorial de n si n es igual o mayor que 0, o None si n es negativo.

# Escriba, además, en el fichero main.py, un programa que, apoyándose en la función anterior, muestre el
# factorial de los números desde -1 a 6, ambos inclusive.

#==============================================================================================================================

import funciones
n = int(input("Di un número: "))
print(funciones.factorial(n))