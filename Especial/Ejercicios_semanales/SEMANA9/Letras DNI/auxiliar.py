def add_letter(dni):
    number = int(dni)
    mod = number % 23
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    return dni + letters[mod]
