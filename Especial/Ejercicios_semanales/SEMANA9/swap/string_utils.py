# Escriba aquí su código
def swap(text):
    words = text.split()
    words = words[::-1]
    words = [word[0].upper() + word[1:].lower() for word in words]
    return ' '.join(words)
