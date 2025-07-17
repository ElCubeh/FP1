# Se han estado midiendo diariamente las temperaturas máximas y mínimas en grados Celsius en una población. Los datos de cada día 
# forman una tupla de dos valores (max, min). Los días se han agrupado por semanas en tuplas-semana de 7 elementos. Finalmente, se
# ha creado una lista con una secuencia de varias semanas.

# Ejemplo:

# datos_semanales = [
#    ((28, 18), (30, 19), (31, 20), (29, 18), (27, 17), (26, 16), (25, 15)),
#    ((32, 21), (33, 22), (34, 23), (32, 20), (29, 18), (27, 17), (25, 15)),
#    ((27, 16), (28, 17), (29, 18), (30, 19), (28, 18), (26, 17), (25, 16))
# ]
# Escriba una función llamada temperaturas_altas(datos_semanales) que tome como parámetro una lista como la descrita y devuelva 
# una nueva lista con las siguientes características:

# La nueva lista tendrá tantos elementos como tuplas-semana tenga la lista original.

# Cada elemento de la nueva lista será una lista cuyos elementos serán las temperaturas máximas de cada día de la semana 
# correspondiente que tengan un valor mayor que el promedio de las temperaturas máximas diarias a lo largo de todo el periodo de 
# tiempo representado. La lista tendrá todos los valores que cumplan dicho criterio, en el orden en que aparecen en la 
# correspondiente tupla-semana original, independientemente de que pueda haber valores repetidos.

# Para poder hacer lo anterior, la función deberá calcular dicho promedio.
# Si en alguna semana no hay ninguna temperatura máxima mayor que el promedio, la lista correspondiente estará vacía.
# Notas:

# La lista original no debe modificarse.
# No puede usarse la función max() predefinida en Python.
# Se valorará positivamente el desarrollo de funciones auxiliares, siempre que sean adecuadas.
# Por ejemplo, para los datos mostrados en el ejemplo anterior, el promedio de temperaturas máximas es aprox. 28.62, por lo que la lista resultante sería:

#[
#    [30, 31, 29], 
#    [32, 33, 34, 32, 29],
#    [29, 30]
#]


# Escriba la función debajo de esta línea

def promedio(lista):
    max = []
    for semana in lista:
        for dia in semana:
            max.append(dia[0])
    promedio = sum(max) / len(max)
    return promedio


def temperaturas_altas(mes):
    result = []
    for semana in mes:
        res = []
        for dia in semana:
            if dia[0] >= promedio(mes):
                res.append(dia[0])
        result.append(res)
    return result


if __name__ == "__main__":
    # Datos de prueba.
    # Si lo desea, puede modificar el ejemplo para probar la función

    datos_semanales = [
        ((28, 18), (30, 19), (31, 20), (29, 18), (27, 17), (26, 16), (25, 15)),
        ((32, 21), (33, 22), (34, 23), (32, 20), (29, 18), (27, 17), (25, 15)),
        ((27, 16), (28, 17), (29, 18), (30, 19), (28, 18), (26, 17), (25, 16))
    ]

    # Construimos la lista de temperaturas supriores al promedio y la mostramos

    result = temperaturas_altas(datos_semanales)
    print(result)