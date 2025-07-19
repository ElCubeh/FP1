import functions

t = (10,  "Pedro", 42, "Margarita", 18.5, 8)

if functions.contains_strs(t):
    print("Hay al menos una string en la tupla", t)
else:
    print("No hay ninguna string en la tupla", t)
