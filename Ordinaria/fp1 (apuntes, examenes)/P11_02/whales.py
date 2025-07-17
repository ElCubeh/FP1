# Se ha estado estudiando un grupo de ballenas y se ha recopilado datos de avistamiento de cada individuo del grupo. A cada
# individuo del grupo se le ha asignado un nombre. Los datos de avistamiento se han almacenado en una lista. Cada elemento de
# esta lista corresponde al avistamiento de un individuo y consiste en una tupla con la fecha (string en formato dd/mm/aaaa) y la
# hora de avistamiento (string en formato hh:mm:ss). 

# Por otra parte, se tiene un diccionario en el que las claves son los nombres asignados a los individuos del grupo de ballenas y
# las contraclaves son tuplas con los índices de los avistamientos de esos individuos en la lista. El diccionario y la lista se
# han juntado en una tupla. 

# Escriba una función, save(sighting, filename), donde sighting es una tupla como la descrita (diccionario, lista) y filename es
# una string. La función debe crear un archivo de texto usando como nombre el valor de filename.

# Cada línea de este archivo contendrá el nombre de un individuo y la secuencia de sus avistamientos, separados por puntos y
# comas (';').

# Las líneas estarán ordenadas alfabéticamente por los nombres de los individuos. Los datos de avistamientos estarán en el orden
# en que aparecen en la lista de índices correspondiente en el diccionario.

# Pista: deberá recorrer el diccionario por la lista ordenada de claves y, para cada clave, formar una línea en el archivo con los
# datos requeridos y escribirla en el archivo. Dado que los avistamientos son una tupla de dos strings, habrá que convertir cada
# avistamiento a string para añadirlo a la línea.



# Escriba aquí la función solicitada

def save(sighting, filename):
    with open(filename, 'w') as seen:
        names = sighting[0]
        names1 = sorted(names.keys())
        see = sighting[1]
        for name in names1:
            seen.write(name)
            for indx in names[name]:
                data0 = str(see[indx][0])
                data1 = str(see[indx][1])
                seen.write(f";('{data0}', '{data1}')")
            seen.write('\n')
        return seen

if __name__ == "__main__":
    sighting = (
        {  # Diccionario {individuos:índices de avistamiento}
            'Whale_A': [0, 4, 5, 6, 7, 8, 10, 11],
            'Whale_B': [0, 1, 2, 3, 6, 7, 11, 12, 13, 19],
            'Whale_C': [2, 4, 12, 13, 15],
            'Whale_D': [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18]
        },
        [  # Lista de avistamientos
            ('01/02/2023', '11:39:15'), ('02/03/2023', '13:22:49'),
            ('23/02/2023', '07:11:45'), ('25/05/2023', '19:58:26'),
            ('19/09/2023', '04:28:23'), ('06/01/2023', '20:41:07'),
            ('07/12/2023', '23:09:13'), ('26/03/2023', '23:55:33'),
            ('16/01/2023', '09:34:55'), ('02/03/2023', '22:16:08'),
            ('23/01/2023', '05:12:49'), ('12/01/2023', '01:26:06'),
            ('19/09/2023', '01:19:35'), ('17/05/2023', '12:54:00'),
            ('16/06/2023', '17:43:15'), ('02/06/2023', '18:08:12'),
            ('17/10/2023', '05:24:34'), ('09/09/2023', '02:48:02'),
            ('13/02/2023', '18:07:13'), ('08/12/2023', '07:46:47')
        ]
    )

    filename = "sighting_data.csv"
    save(sighting, filename)