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
