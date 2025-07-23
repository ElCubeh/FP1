import sqlite3
from utilities import create_db, show, show_file


# Escriba aquí la función solicitada

def import_data(database_name: str, file_name: str) -> None:
    # Establecer conexión con la base de datos
    conexion = sqlite3.connect(database_name)
    cursor = conexion.cursor()
    
    try:
        # Leer el archivo CSV
        with open(file_name, 'r') as archivo:
            lineas = archivo.readlines()
        
        # Procesar cada línea del archivo
        for linea in lineas:
            # Eliminar espacios y dividir por comas
            datos = linea.strip().split(',')
            if len(datos) == 3:
                matricula, marca, kilometraje = datos
                # Actualizar la base de datos si coinciden matrícula y marca
                cursor.execute(
                    "UPDATE coches SET kilometraje = ? WHERE matricula = ? AND marca = ?",
                    (int(kilometraje), matricula, marca)
                )
        
        # Confirmar los cambios
        conexion.commit()
    
    finally:
        # Cerrar la conexión
        conexion.close()

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
