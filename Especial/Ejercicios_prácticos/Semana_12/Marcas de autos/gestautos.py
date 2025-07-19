# Escriba aquí la función solicitada
def marcas(autos):
    marcas_unicas = set()
    with open(autos, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            datos = linea.split(',')
            if len(datos) >= 2:
                marcas_unicas.add(datos[1])
    lista_marcas = sorted(marcas_unicas)

    return lista_marcas


if __name__ == "__main__":
    lista_de_marcas = marcas("data.csv")
    print(lista_de_marcas)
