# Escriba aquí su código
import auxiliar


def change_dict(dicionario):
    for key, value in dicionario.items():
        dicionario[key] = (auxiliar.add_letter(key), value)
