import file_utils
from string_utils import read_csv_selecting_fields

datos = read_csv_selecting_fields("clients_data.csv", ["nombre", "ciudad"])
for registro in datos:
    print(registro)
