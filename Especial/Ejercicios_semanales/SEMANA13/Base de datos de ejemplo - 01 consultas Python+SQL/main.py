import sqlite3

db = sqlite3.connect('base_de_datos.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()
# cursor.execute("SELECT * FROM Productos WHERE descripcion like 's%'")
# cursor.execute("SELECT * FROM Productos WHERE existencias <= stockminimo")
cursor.execute("SELECT * FROM clientes WHERE provincia = 'Valencia'")
data = cursor.fetchall()
if len(data) > 0:
    for field_name in data[0].keys():
        print(field_name, end=' | ')
    print()
    for record in data:
        for field_value in record:
            print(field_value, end=' | ')
        print()
db.close()
