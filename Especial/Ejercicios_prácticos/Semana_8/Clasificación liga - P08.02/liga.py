from auxiliar import show


# Escriba aquí la función
def clasificación(liga):
    def getkey(tupla):
        equipo, puntos = tupla
        return puntos
    lista = [
        (equipo, 3 * ganados + 1 * empatados)
        for equipo, (ganados, empatados, perdidos) in liga.items()
        ]
    lista.sort(key=getkey, reverse=True)
    return lista


if __name__ == "__main__":
    liga_petanca = {
        "Lobos grises": (4, 3, 1),
        "Damas de la noche": (3, 2, 3),
        "Los de aquí": (2, 3, 3),
        "Los de allí": (3, 1, 4),
        "Las del otro lado": (2, 3, 3)
    }
    lst_clasificación = clasificación(liga_petanca)
    show(lst_clasificación)
