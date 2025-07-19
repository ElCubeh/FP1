import sqlite3
from utilities import create_db, show

# Escriba aquí la función solicitada


if __name__ == "__main__":
    """
    --------------MENÚ----------------
    Entrantes calientes:
        - Sopa de ajo            8.00€
        - Sopa de tomate         4,50€
        - Croquetas de jamón     6,50€
        - Calamares a la romana  9,50€
    Entrantes fríos:
        - Ensalada César         7,50€
        - Gazpacho               5,00€
        - Carpaccio de salmón   10.00€
    De cuchara:
        - Lentejas               6,00€
        - Sopa de mariscos       9,00€
        - Crema de calabaza      5,50€
    Hamburguesas:
        - Small Mac              4,50€
        - Cheese King            4,75€
    """

    create_db("menu.db")
    servicio = [
        "Sopa de tomate", "Ensalada Cesar", "Sopa de tomate",
        "Gazpacho", "Gazpacho"
    ]

    print("Resultado devuelto por la función:", cuenta(servicio))
