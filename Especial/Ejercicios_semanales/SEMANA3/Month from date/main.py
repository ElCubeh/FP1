from string_utils import month

if __name__ == "__main__":
    # Datos iniciales
    date = "01-06-1970"

    # Cálculo y presentación del resultado
    result = month(date)
    print("El mes en", date, "es", result)
