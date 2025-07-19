# Escriba aquí su código
def filter_names(names, letter):
    if not names:
        return[]
    if names[0][0] == letter:
        return [names[0]] + filter_names(names[1:], letter)
    else:
        return filter_names(names[1:], letter)
