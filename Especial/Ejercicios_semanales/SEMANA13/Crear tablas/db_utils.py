# Escriba aquí su código
import csv
import sqlite3


def create_tables(conn, fichero_csv):
    with open(fichero_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            table_name = row[0]
            fields = row[1:]
            field_str = ', '.join(fields)
            query = f'CREATE TABLE IF NOT EXISTS {table_name} ({field_str})'
            conn.execute(query)
