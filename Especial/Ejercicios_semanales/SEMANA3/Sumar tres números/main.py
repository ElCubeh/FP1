# Escriba su código aquí
def suma(a , b, c):
    return a + b + c
# No modifique el código por debajo de esta línea
if __name__ == "__main__":
    # Petición de datos
    print("___Se van a sumar tres números___")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    num3 = int(input("Tercer número: "))

    # Cálculo y presentación del resultado
    result = suma(num1, num2, num3)
    print("Resultado:", result)
