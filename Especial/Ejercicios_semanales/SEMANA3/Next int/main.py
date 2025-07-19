from numbers import next_int

if __name__ == "__main__":
    # Petición de datos
    num = int(input("Dame un número: "))

    # Cálculo y presentación del resultado
    sig = next_int(num)
    print("El número que sigue a", num, "es", sig)
