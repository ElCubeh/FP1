# Escriba aquí su código
import csv
def export_dict(dict_to_export, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in dict_to_export.items():
            writer.writerow([key] + list(value))
