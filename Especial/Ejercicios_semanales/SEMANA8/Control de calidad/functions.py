# Escriba aquí su código
def fallo_HD(HD, BD):
    solo_HD = set()
    for id in HD:
        if id not in BD:
            solo_HD.add(id)
    return solo_HD
