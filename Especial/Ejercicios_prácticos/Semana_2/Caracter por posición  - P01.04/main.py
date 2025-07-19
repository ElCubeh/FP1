texto = input("Ingresa un texto: ")
index = int(input(f"Ingresa un número menor que {len(texto) - 1}:"))
print(f"El carácter en esa posición es: {texto[index]}")