from auxiliar import show
import file_utils
import string_utils
"""Módulo para ejecutar y comprobar el resultado."""
"""La función donantes debe escribirse en el fichero 'string_utils.py'"""


print("Contenido del fichero:")
print("----------------------")
file_utils.show_file(file_utils.filename("input.csv"))
print("\n-------------------------------------------------------------------")
print("Diccionario resultante:")
print("-----------------------")
show(string_utils.donantes(file_utils.filename("input.csv")))
