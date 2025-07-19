import sqlite3
from utilities import create_db, show

# Escriba aquí la función solicitada


if __name__ == "__main__":
    create_db("menu.db")
    print("BBDD original------------------------------------------")
    show("menu.db")

    filename = "menu.csv"
    print("Resultado devuelto por la función----------------------")
    print(cargar_platos(filename))

    print("BBDD final---------------------------------------------")
    show("menu.db")
