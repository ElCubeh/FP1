# Se han recopilado datos sobre las precipitaciones de lluvia (litros/m2) en una población durante un año y se ha almacenado
# en una lista. Esta lista tiene 12 valores que representan la cantidad de lluvia contabilizada cada mes, de enero a diciembre,
# en esa población. Por ejemplo:

# [12.8, 10.5, 6.7, 5.3, 3.4, 2.8, 1.5, 0.5, 0.7, 2.0, 6.8, 10.3]
# Desarrolle una función mes_mas_lluvioso(lluvias), donde lluvias es una lista como la descrita. Esta función, sin usar la
# función max() de Python, debe devolver el nombre del mes en que más ha llovido. Los nombres de los meses son:  "enero",
# "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre" y "diciembre".
# Si hay varios meses en los que ha llovido la cantidad máxima, se devolverá el primero.


def mes_mas_lluvioso(lista):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    for mes in lista:
        p = lista[0]
        if mes >= p:
            res = mes
            ind = lista.index(res)
    return meses[ind]



if __name__ == "__main__":
    lluvias = [12.8, 10.5, 6.7, 5.3, 3.4, 2.8, 1.5, 0.5, 0.7, 2.0, 6.8, 10.3]
    mes = mes_mas_lluvioso(lluvias)
    print("El mes más lluvioso fue:", mes)
