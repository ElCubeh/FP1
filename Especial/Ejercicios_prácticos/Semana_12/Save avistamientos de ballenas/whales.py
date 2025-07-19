from utilities import show
# Escriba aquí la función solicitada


def save(sighting, filename):
    sighting_dict, avistamientos_lista = sighting
    with open(filename, 'w') as archivo:
        for nombre in sorted(sighting_dict.keys()):
            indices = sighting_dict[nombre]
            sighting = [avistamientos_lista[i] for i in indices]
            sighting_str = ';'.join([f"('{fecha}', '{hora}')" for fecha, hora in sighting])
            archivo.write(f'{nombre};{sighting_str}\n')


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
    show(filename)
