"""Se tiene un diccionario con información sobre una competición de liga. 
Las claves son los nombres de los equipos que participan en la competición y los valores 
son tuplas con el número de partidos ganados, empatados y perdidos por el equipo correspondiente.

Escriba una función, mejor(liga, equipos), donde liga es un diccionario con la estructura 
descrita y equipos es una lista de nombres de equipos. La función debe devolver el nombre 
del equipo que más puntos tenga de los incluidos en la lista (un equipo suma 3 puntos por 
cada partido ganado y 1 punto por cada partido empatado). La lista podrá contener nombres 
que no correspondan con equipos de la liga, lo cuál no afectará al calculo, dando por 
supuesto que siempre habrá en la lista al menos un nombre correcto. 
Si hay más de un equipo con la misma puntuación, se devolverá el que esté primero 
en la lista."""

# Escriba aquí la función
def mejor(liga, equipos):
    max_p = -1
    m_equipo = None
    for equipo in equipos:
        if equipo in liga:
            p_ganados, p_empatados, p_perdidos = liga[equipo]
            puntos = p_ganados * 3 + p_empatados * 1
            if puntos > max_p:
                max_p = puntos
                m_equipo = equipo
    return m_equipo


if __name__ == "__main__":
    liga_petanca = {
        "Lobos grises": (4, 3, 1),
        "Damas de la noche": (3, 2, 3),
        "Los de aquí": (2, 3, 3),
        "Los de allí": (3, 1, 4),
        "Las del otro lado": (2, 3, 3)
    }
    equipos = ["Los de aquí", "uno erróneo", "Los de allí"]
    mejor_clasificado = mejor(liga_petanca, equipos)
    print(f"El equipo mejor clasificado es: {mejor_clasificado}")