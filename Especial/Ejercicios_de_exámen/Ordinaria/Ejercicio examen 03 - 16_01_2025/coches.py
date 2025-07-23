import sqlite3
from utilities import create_db, show, show_file


# Escriba aquí la función solicitada
def export_data(database_name: str, file_name: str, brand: str) -> None:
    # Conectar a la base de datos
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # Consulta SQL para obtener los datos requeridos
    query = "SELECT matricula, modelo, año FROM coches WHERE marca = ?"
    cursor.execute(query, (brand,))
    
    # Recuperar todos los resultados
    results = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()
    
    # Escribir los resultados en el archivo
    with open(file_name, 'w', encoding='utf-8') as file:
        for row in results:
            # Formatear cada fila como matricula,modelo,año
            line = f"{row[0]},{row[1]},{row[2]}\n"
            file.write(line)

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
