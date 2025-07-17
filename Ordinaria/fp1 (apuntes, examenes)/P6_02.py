# Se han estado registrando las temperaturas máximas y mínimas diarias en grados Celsius. Los datos de cada día forman una tupla
# de dos valores (tmax, tmin). Los días se han agrupado por semanas en tuplas de siete elementos. Finalmente, se ha creado una
# lista con una secuencia correspondiente a varias semanas.

# Escriba una función llamada maxima_semana que tome como parámetro una lista como la descrita y devuelva una nueva lista con
# las temperaturas máximas semanales. No use la función max() de Python.

# Ejemplo:

# datos_semanales = [
#     ((28, 18), (30, 19), (31, 20), (29, 18), (27, 17), (26, 16), (25, 15)),
#     ((32, 21), (33, 22), (34, 23), (32, 20), (29, 18), (27, 17), (25, 15)),
#     ((27, 16), (28, 17), (29, 18), (30, 19), (28, 18), (26, 17), (25, 16))
# ]
# temperaturas_maximas = maxima_semana(datos_semanales)
# print(temperaturas_maximas) ==> muestra [31, 34, 30]


def maxima_semana(lista):

    res = []
    

    for semana in lista:
        max = semana[0][0]
        for dia in semana:
            if dia[0] > max:
                max = dia[0]
        res.append(max)
    return res




if __name__ == "__main__":
    # Si lo desea, puede modificar el ejemplo para probar la función

    datos_semanales = [
        ((28, 18), (30, 19), (31, 20), (29, 18), (27, 17), (26, 16), (25, 15)),
        ((32, 21), (33, 22), (34, 23), (32, 20), (29, 18), (27, 17), (25, 15)),
        ((27, 16), (28, 17), (29, 18), (30, 19), (28, 18), (26, 17), (25, 16))
    ]

    temperaturas_maximas = maxima_semana(datos_semanales)
    print(temperaturas_maximas)
