# Escriba aquí su código
def chars_frecs(s):
    frecuencias = {}
    for char in s:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias
