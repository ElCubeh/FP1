"""La información sobre los partidos de una liga deportiva se almacena en una lista. Cada elemento de la lista 
representa un partido y es una tupla de cuatro valores: el nombre del equipo local, el número de goles marcados por el equipo local, 
el nombre del equipo visitante y el número de goles marcados por el equipo visitante.

Escriba una función, score(league), donde league es una lista como la descrita. 
La función debe devolver un diccionario en el que las claves sean los nombres de los equipos y 
los valores sean tuplas de dos elementos: el número total de goles marcados como local y el número total de goles marcados como visitante por 
el equipo correspondiente.
"""

def score(league):
    scores = {}

    for match in league:
        local_team, local_goals, visitor_team, visitor_goals = match

        if local_team not in scores:
            scores[local_team] = (0, 0) 
        local_local_goals, local_visitor_goals = scores[local_team]
        scores[local_team] = (local_local_goals + local_goals, local_visitor_goals)

        if visitor_team not in scores:
            scores[visitor_team] = (0, 0)
        visitor_local_goals, visitor_visitor_goals = scores[visitor_team]
        scores[visitor_team] = (visitor_local_goals, visitor_visitor_goals + visitor_goals)

    return (scores)

if __name__ == "__main__":
    matchs = [
    ('Murcia', 5, 'Valencia', 1),
    ('Murcia', 2, 'Alicante', 1),
    ('Almería', 3, 'Alicante', 3),
    ('Alicante', 0, 'Zamora', 1),
    ('Zamora', 5, 'Castellón', 3),
    ('Murcia', 5, 'Castellón', 1),
    ('Alicante', 4, 'Castellón', 3),
    ('Murcia', 4, 'Almería', 0),
    ('Castellón', 2, 'Zamora', 1),
    ('Valencia', 0, 'Murcia', 1),
    ('Zamora', 4, 'Alicante', 2),
    ('Valencia', 2, 'Castellón', 2),
    ('Castellón', 4, 'Valencia', 3),
    ('Valencia', 1, 'Alicante', 1),
    ('Almería', 5, 'Murcia', 2),
    ('Zamora', 1, 'Valencia', 3),
    ('Valencia', 0, 'Zamora', 0),
    ('Murcia', 5, 'Castellón', 1),
    ('Valencia', 4, 'Almería', 3),
    ('Castellón', 5, 'Murcia', 0),
    ('Almería', 4, 'Castellón', 3),
    ('Castellón', 4, 'Alicante', 3),
    ('Alicante', 0, 'Murcia', 3),
    ('Murcia', 5, 'Zamora', 1),
    ('Alicante', 0, 'Valencia', 3),
    ('Alicante', 1, 'Almería', 0),
    ('Zamora', 3, 'Murcia', 2),
    ('Zamora', 5, 'Almería', 0),
    ('Almería', 1, 'Valencia', 1),
    ('Castellón', 1, 'Almería', 3),
    ('Almería', 0, 'Zamora', 2)
]
    print(score(matchs))