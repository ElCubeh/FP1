# Escriba un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable.
# A continuación, debe solicitar al usuario que ingrese un número positivo menor que la cantidad de caracteres que
# tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 3)
# y mostrar en pantalla el carácter del texto ubicado en la posición dada por dicho número.

# ==============================================================================================================================

# Ejemplo de ejecución:

# Ingresa un texto: En un lugar de La Mancha, de cuyo nombre no quiero acordarme...
# Ingresa un número menor que 63: 7
# El carácter en esa posición es: u

text = input("Introduce un texto: ")
index = int(input(f"Introduce un número menor que {len(text)-1}: "))
print(text[index])