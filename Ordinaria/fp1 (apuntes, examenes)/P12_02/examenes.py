#La información sobre los exámenes realizados en una asignatura se ha guardado en una base de datos Sqlite3 llamada examenes.db 
# con la siguiente estructura:

#CREATE TABLE examenes(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    descripción TEXT UNIQUE NOT NULL
#    peso REAL
#);
#CREATE TABLE estudiantes(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre TEXT UNIQUE NOT NULL
#); 
#CREATE TABLE resultados(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    examen_id INTEGER NOT NULL,
#    estudiante_id INTEGER NOT NULL,
#    nota REAL,
#    FOREIGN KEY(examen_id) REFERENCES examenes(id),
#    FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
#);
#Notas:

#Los campos marcados como PRIMARY KEY AUTOINCREMENT son automáticos; no se deben insertar valores para dichos campos al añadir una
#fila nueva a la tabla.

#El modificador UNIQUE significa que el campo no va a tener valores repetidos y el modificador NOT NULL significa que no puede 
# estar vacío (tener valor null).

#La línea FOREIGN KEY(categoria_id) REFERENCES categoria(id) indica que todo valor del campo categoria_id de un plato se tiene que 
#corresponder con el valor del id de alguna categoría en la tabla categorías.

#Escriba una función nota_final(estudiante) que, dado el nombre de un estudiante, devuelva su nota final. La nota final se calcula 
#como la suma de los resultados de multiplicar la nota obtenida en cada examen por el peso de ese examen.


import sqlite3


# Escriba aquí la función solicitada

def nota_final(estudiante):
    db = sqlite3.connect("examenes.db")
    cursor = db.cursor()
    nota_final = 0

    nombre_sql = f"SELECT id FROM resultados WHERE nombres = '{estudiante}';"



if __name__ == "__main__":
    print("BBDD original------------------------------------------")

    print("Resultado devuelto por la función----------------------")
    estudiante = "Pedro Bénitez Gómez"
    print(nota_final(estudiante))