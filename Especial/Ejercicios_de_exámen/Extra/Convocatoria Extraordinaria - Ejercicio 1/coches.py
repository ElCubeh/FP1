import re

# Escriba aquí la función solicitada


if __name__ == "__main__":
    coches = {
        "ABC123": ["Toyota", "Camry", "3018", 50000],
        "DEF446": ["Ford", "Focus", "2017", 40000],
        "GHI789": ["Toyota", "Corolla", "2019", 60000],
        "JKL012": ["Chevrolet", "Cruze", "2016"],
    }
    cambios = [
        ("DEF446", 45000),  # Correcto y está
        ("KLMO98", 70000),  # Incorrecto
        ("KLM098", 75000)   # Correcto pero no está
    ]
    resultado = import_data(coches, cambios)
    print(coches, "\n")
    print(resultado)
