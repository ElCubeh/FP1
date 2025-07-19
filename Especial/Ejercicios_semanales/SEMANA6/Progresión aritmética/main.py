import functions

print("Se va a generar una progresión aritmética")
inicial = int(input("Valor inicial: "))
incremento = int(input("Distancia: "))
cuantos = int(input("Nº de valores a generar: "))
frecs = functions.progresion(inicial, incremento, cuantos)
print(frecs)
