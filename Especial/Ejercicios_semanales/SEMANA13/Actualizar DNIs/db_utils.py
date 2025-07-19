# Escriba aquí su código
import sqlite3
from string_utils import dni_letter


def update_dnis(conn):
    cur = conn.cursor()
    cur.execute("Select dni FROM Persons")
    rows = cur.fetchall()
    for row in rows:
        dni_ = row[0] + dni_letter(row[0])
        cur.execute("UPDATE Persons SET dni = ? WHERE dni = ?", (dni_, row[0]))
    conn.commit()
    cur.close()
