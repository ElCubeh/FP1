from measurements import km2mi

if __name__ == "__main__":
    # Petición de datos
    print("___Se va aconvertir de Kilómetros a millas___")
    km = int(input("Kilometros: "))

    # Cálculo y presentación del resultado
    mi = km2mi(km)
    print("Equivalen a:", mi, "millas")
