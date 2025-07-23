import re

def import_data(data, updates):
    invalid_or_missing = []
    pattern = r'^[A-Z]{3}\d{3}$'  # Patrón para 3 letras mayúsculas + 3 dígitos
    
    for plate, mileage in updates:
        # Verificar formato de matrícula
        if not re.match(pattern, plate):
            invalid_or_missing.append(plate)
            continue
        
        # Verificar existencia en el diccionario y actualizar kilometraje
        if plate in data:
            data[plate][3] = mileage  # Actualizar el cuarto elemento (kilometraje)
        else:
            invalid_or_missing.append(plate)
    
    return invalid_or_missing

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
