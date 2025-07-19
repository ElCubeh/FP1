from string_utils import transform_date

if __name__ == "__main__":
    # Datos iniciales
    date = "01-06-1970"

    # Cálculo y presentación del resultado
    result = transform_date(date)
    print("La fecha", date, "transformada es", result)
