# Se tiene un diccionario con información sobre una competición de liga. Las claves son los nombres de los equipos que participan
# en la competición y los valores son tuplas con el número de partidos ganados, empatados y perdidos por el equipo correspondiente.

# Escriba una función, clasificación(liga), donde liga es un diccionario con la estructura descrita. La función debe devolver una
# lista de tuplas. El primer valor de cada tupla será el nombre de un equipo y el segundo el número de puntos obtenidos por ese
# equipo. los equipos mantendrán el orden que tenían en el diccionario. Un equipo suma 3 puntos por cada partido ganado y 1 punto
# por cada partido empatado.


# Escriba aquí la función
def clasificación(liga):
    res = []
    for equipo in liga:
        juegos = liga.get(equipo)
        total_puntos = juegos[0]*3 + juegos[1]
        r = (equipo, total_puntos)
        res.append(r)
    return res




if __name__ == "__main__":
    liga_petanca = {
        "Lobos grises": (4, 3, 1),
        "Damas de la noche": (3, 2, 3),
        "Los de aquí": (2, 3, 3),
        "Los de allí": (3, 1, 4),
        "Las del otro lado": (2, 3, 3)
    }
    lst_clasificación = clasificación(liga_petanca)
    print(lst_clasificación)