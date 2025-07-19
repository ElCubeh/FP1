import string_utils

frecs = (
    {"Esto": 2, "una": 4, "otro": 2, "el": 10, "esdrújula": 1, "pantufla": 2},
    21
)
formatted = string_utils.format_frecs(frecs)

for line in formatted:
    print(line)
