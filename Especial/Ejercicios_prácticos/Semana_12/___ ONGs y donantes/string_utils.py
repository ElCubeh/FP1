# escriba aquí su código
def donantes(filename):
    ong_donantes = {}
    with open(filename, 'w', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            datos = linea.split(',')
            ong = datos[0].strip()
            donantes = [donante.strip()for donante in datos[1:]]
            ong_donantes[ong] = donantes
    return ong_donantes
    