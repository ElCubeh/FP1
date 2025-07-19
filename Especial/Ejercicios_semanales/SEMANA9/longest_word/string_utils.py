# Escriba aquí su código
def longest_word(input_str):
    words = input_str.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
