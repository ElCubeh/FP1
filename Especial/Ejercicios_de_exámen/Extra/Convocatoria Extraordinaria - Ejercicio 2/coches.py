import sqlite3
from utilities import create_db, show, show_file


# Escriba aquí la función solicitada


if __name__ == "__main__":
    create_db("concesionario.db")
    print("--- Base de Datos original ---")
    show("concesionario.db")
    print("--- Fichero ---")
    show_file("concesionario.csv")

    bbdd = "concesionario.db"
    file = "concesionario.csv"

    import_data(bbdd, file)

    print("\n--- Base de Datos resultante ---")
    show("concesionario.db")
