# Escriba aquí la función
def maxima_semana(lista_semanas):
    maximo_semanales = []
    for semana in lista_semanas:
        max_semanal = semana[0][0]
        for dia in semana:
            for temp in dia:
                if temp > max_semanal:
                    max_semanal = temp
        maximo_semanales.append(max_semanal)
    return maximo_semanales


if __name__ == "__main__":
    # Si lo desea, puede modificar el ejemplo para probar la función

    datos_semanales = [
        ((28, 18), (30, 19), (31, 20), (29, 18), (27, 17), (26, 16), (25, 15)),
        ((32, 21), (33, 22), (34, 23), (32, 20), (29, 18), (27, 17), (25, 15)),
        ((27, 16), (28, 17), (29, 18), (30, 19), (28, 18), (26, 17), (25, 16))
    ]

    temperaturas_maximas = maxima_semana(datos_semanales)
    print(temperaturas_maximas)
