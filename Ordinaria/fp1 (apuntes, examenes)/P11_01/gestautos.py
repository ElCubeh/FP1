# Una compañía de venta de automóviles usados ha almacenado la información de su stock en un archivo de texto. Cada línea de este
# archivo se compone de los siguientes datos, separados por comas: matrícula, marca, modelo, año de matriculación y kilómetros.

# Por ejemplo:

# ABC123,Toyota,Camry,2018,50000
# DEF456,Ford,Focus,2017,40000
# GHI789,Toyota,Corolla,2019,60000
# JKL012,Chevrolet,Cruze,2016,30000
# MNO345,Ford,Mustang,2020,70000
# PQR678,Chevrolet,Spark,2015,20000

# Escriba una función marcas(autos), donde el parámetro autos es el nombre de un archivo de texto existente que contiene la
# información descrita. La función debe devolver una lista ordenada alfabéticamente con los nombres de las marcas que aparecen en
# el archivo. Cada marca debe aparecer una sola vez, y la lista de marcas debe estar ordenada en orden alfabético ascendente.

# Escriba aquí la función solicitada

def marcas(text):
    with open(text, 'r') as f:
        lineas = f.readlines()

        marcas = []

        for linea in lineas:
            datos = linea.split(',')
            if datos[1] not in marcas:
                marcas.append(datos[1])
    
    marcas.sort()
    return marcas



if __name__ == "__main__":
    lista_de_marcas = marcas("data.csv")
    print(lista_de_marcas)
