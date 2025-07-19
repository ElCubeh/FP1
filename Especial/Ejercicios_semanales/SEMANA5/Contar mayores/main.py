import functions

t = (8.0, 20.8, 14.5, 3.9, 18.3, 14.8)
umbral = 15.0

cuenta = functions.contar_mayores(t, umbral)
print("Hay", cuenta, "valores mayores que", umbral, "en la tupla", t)
