# Escriba aquí su código
def isvowel(string):
    vowels = "aeiouüáéíóúAEIOUÜÁÉÍÓÚ"
    for char in string:
        if char not in vowels:
            return False
    return True
