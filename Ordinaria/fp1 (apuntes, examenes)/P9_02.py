# Una multilista de enteros es una lista en que cada elemento puede ser un número entero o una multilista de enteros (véase el
# ejemplo).

# Se pide escribir una función RECURSIVA llamada multisuma que tome como parámetro una multilista de enteros y devuelva la suma
# de todos los números enteros contenidos en la misma, tanto directamente como en cualquiera de las listas que contiene. Para la
# multilista de la figura, el resultado que debería dar la función es: 

# 348 = (35+14+((12+34)+14+98)+10+12+28+(56+((10+14)+(11))))

# Escriba aquí su código

def multisuma(lista):
    if isinstance(lista, list):
        return sum(multisuma(x) for x in lista)
    else:
        return lista

if __name__ == "__main__":
    lista_de_prueba = [
        35, 14,
        [
            [12, 34],
            14, 98,
        ],
        10, 12, 28,
        [
            56,
            [
                [10, 14],
                [11]
            ]
        ]
    ]
    print(multisuma(lista_de_prueba))