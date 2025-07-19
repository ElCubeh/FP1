from finanzas import capital

if __name__ == "__main__":
    # Petición de datos
    print("___Se va a calcular el capital final después de n periodos___")
    inicial = float(input("Capital incial: "))
    interés = float(input("Tasa de interés en tanto por 1 (4% = 0.04): "))
    periodos = int(input("Número de periodos: "))

    # Cálculo y presentación del resultado
    final = capital(inicial, interés, periodos)
    print("Capital final", final)
