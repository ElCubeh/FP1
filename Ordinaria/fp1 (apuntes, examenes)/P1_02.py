# Escriba un programa que solicite al usuario un número y le reste el 15%.
# A continuación, debe mostrar el resultado final en pantalla.

# ==============================================================================================================================

# Ejemplo de ejecución:

# ¿Número? : 260
# Descontado el quince por ciento queda: 221.0

num = int(input("¿Número?: "))
porcentaje = num * 15 / 100
print(f"Descontado el quince por ciento, queda: {num - porcentaje}")