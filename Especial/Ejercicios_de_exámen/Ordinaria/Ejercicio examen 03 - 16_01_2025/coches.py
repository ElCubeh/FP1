import sqlite3
from utilities import create_db, show, show_file


# Escriba aquí la función solicitada


if __name__ == "__main__":
    create_db("concesionario.db")
    print("--- Base de Datos original ---")
    show("concesionario.db")

    bbdd = "concesionario.db"
    file = "concesionario.csv"
    marca = "Toyota"

    export_data(bbdd, file, marca)

    print("\n--- Contenido del fichero resultante ---")
    show_file(file)
