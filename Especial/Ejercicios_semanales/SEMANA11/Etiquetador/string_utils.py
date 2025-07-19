# Escriba aquí su código
def tagger(text, alphabet):
    words = text.split()
    new_words = []
    for word in words:
        if all(char in alphabet for char in words):
            new_word = "[target]" + word + "[endtarget]"
            new_words.append(new_word)
        else:
            new_words.append(word)
    return " ".join(new_words)
