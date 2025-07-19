from measurements import celsius2fahrenheit

if __name__ == "__main__":
    # Petición de datos
    print("___Se va aconvertir de grados Celsius a Fahrentheit___")
    celsius = int(input("Temperatura en grados Celsius: "))

    # Cálculo y presentación del resultado
    fahrenheit = celsius2fahrenheit(celsius)
    print(fahrenheit)
