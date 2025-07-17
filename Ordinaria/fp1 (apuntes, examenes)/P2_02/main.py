# Un año bisiesto es uno que es divisible por 4 y no por 100 (secular no bisiesto), o que es divisible por 400 (secular bisiesto).

# Escriba, en el archivo funciones.py una función, es_bisiesto(año), donde año referencia un número entero que representa un año.
# La función debe devolver True si el año es bisiesto; en otro caso, debe devolver False.

# Nota: resuelva el problema sin utilizar operadores booleanos

# Escriba también, en el archivo main.py, un programa que, para ilustrar el uso de la función, la llame con distintos valores
# de año (no bisiesto, bisiesto secular, bisiesto no secular).

#==============================================================================================================================

from P2_03.funciones import es_bisiesto

print(es_bisiesto(100))
print(es_bisiesto(400))
print(es_bisiesto(104))
print(es_bisiesto(2024))
