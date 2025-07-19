import db_utils
import sqlite3
import dataset_utils

db = sqlite3.connect("ProductsCustomersAndSupliers")
db_utils.create_tables(db, "tables.csv")

for table in dataset_utils.list_tables(db):
    print(table)

db.close()
