import db_utils
import sqlite3
import dataset_utils

db = sqlite3.connect("PersonsDB")

dataset_utils.load_dataset(db, "persons.sql")  # Inicializa la DB de prueba
db_utils.update_dnis(db)

for row in dataset_utils.get_table_data(db, "Persons"):
    print(row)

db.close()
