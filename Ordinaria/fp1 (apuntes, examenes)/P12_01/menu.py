# Se tiene una base de datos SQLite3 llamada menu.db, que representa el menú de un restaurante, con las siguientes tablas:

# CREATE TABLE categorias(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre TEXT UNIQUE NOT NULL
# );

# CREATE TABLE platos(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre TEXT UNIQUE NOT NULL,
#    precio REAL,   
#    categoria_id INTEGER NOT NULL,
#    FOREIGN KEY(categoria_id) REFERENCES categorias(id)
# );
# Notas:

# Los campos marcados como PRIMARY KEY AUTOINCREMENT son automáticos; no se deben insertar valores para dichos campos al añadir
# una fila nueva a la tabla.

# El modificador UNIQUE significa que no se permiten valores repetidos y el modificador NOT NULL significa que el campo no puede
# estar vacío (tener valor null).

# La línea FOREIGN KEY(categoria_id) REFERENCES categoria(id) indica que todo valor del campo categoria_id de un plato se tiene
# que corresponder con el valor del id de alguna categoría en la tabla categorías.

# Escriba una función llamada cargar_platos que admita un parámetro de tipo str y devuelva un resultado de tipo list, o True.

# El parámetro de la función representa el nombre de un fichero de texto. Cada línea de este fichero contendrá, separadas por el
# carácter ';', el nombre de una categoría, el nombre de un plato y el precio de un plato; por ejemplo:

# entrantes;papas arrugadas;12.0

# La función cargar_platos deberá insertar en la tabla platos los platos enumerados en el fichero, junto con el código de
# identificación de su categoría.

# Si algún plato tiene una categoría que no existe en la tabla categorias, una tupla formada por el nombre de la categoría y el
# nombre del plato se insertará en una lista que contendrá todos los platos con categorías incorrectas y que se devolverá al final
# de la ejecución de la función.

# Si al final de la ejecución de la función la lista de platos con categorías incorrectas está vacía (porque no se ha encontrado
# ninguno), la función devolverá True en vez de una lista vacía.

import sqlite3

# Escriba aquí la función solicitada

def cargar_platos(file):
    db = sqlite3.connect("menu.db")

    cursor = db.cursor()

    with open(file, 'r') as f:
        lines = f.readlines()

    platos_categorias_incorrectas = []
    platos_correctos = []

    for linea in lines:
            categoria, plato, precio = linea.strip().split(';')

            try:
                cursor.execute("INSERT INTO platos (nombre, precio,categoria_id) VALUES (?, ?, (SELECT id FROM categorias WHERE nombre = ?))", (plato, precio, categoria))
            except sqlite3.IntegrityError:
                platos_categorias_incorrectas.append((categoria, plato))
            else:
                platos_correctos.append((categoria, plato, precio))

    db.commit()
    db.close()
    if platos_categorias_incorrectas:
        return platos_categorias_incorrectas
    else:
        return True

if __name__ == "__main__":
    print("BBDD original------------------------------------------")

    filename = "menu.db"
    print("Resultado devuelto por la función----------------------")
    print(cargar_platos(filename))

    print("BBDD final---------------------------------------------")