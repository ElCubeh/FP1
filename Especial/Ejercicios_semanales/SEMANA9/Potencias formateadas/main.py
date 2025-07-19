import pows

if __name__ == "__main__":
    # Petición de datos
    num = int(input("Dame un número entre 0 y 10: "))

    # Cálculo y presentación del resultado
    print(pows.format_pows(num))
