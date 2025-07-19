# Escriba aquí su código
import csv

def read_csv_selecting_fields(file_name, fields_selected):
    data = []
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fieldnames = next(csvreader)
        fields_selected_indices = [fieldnames.index(field) for field in fields_selected]
        for row in csvreader:
            selected_row = [row[i] for i in fields_selected_indices]
            data.append(selected_row)
    return data
