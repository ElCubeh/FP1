import sqlite3
from utilities import create_db, show


# Escriba aquí la función solicitada


if __name__ == "__main__":
    create_db("examenes.db")
    print("BBDD original------------------------------------------")
    show("examenes.db")

    print("Resultado devuelto por la función----------------------")
    estudiante = "Pedro Bénitez Gómez"
    print(nota_final(estudiante))
