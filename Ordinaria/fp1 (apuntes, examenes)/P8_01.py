# Se tiene un diccionario con información sobre una competición de liga. Las claves son los nombres de los equipos que participan
# en la competición y los valores son tuplas con el número de partidos ganados, empatados y perdidos por el equipo correspondiente.

# Escriba una función, puntuación(liga), donde liga es un diccionario con la estructura descrita. La función debe modificar el
# diccionario de forma que los valores pasen a ser tuplas de dos valores, el primero la tupla original y el segundo el número de
# puntos obtenidos por el equipo correspondiente. Un equipo suma 3 puntos por cada partido ganado y 1 punto por cada partido
# empatado.

# Escriba aquí la función

def puntuación(liga):
    for k in liga:
        liga[k] = (liga[k], liga[k][0] * 3 + liga[k][1])
    return liga
        

if __name__ == "__main__":
    liga_petanca = {
        "Lobos grises": (4, 3, 1),
        "Damas de la noche": (3, 2, 3),
        "Los de aquí": (2, 3, 3),
        "Los de allí": (3, 1, 4),
        "Las del otro lado": (2, 3, 3)
    }
    puntuación(liga_petanca)
    print(liga_petanca)