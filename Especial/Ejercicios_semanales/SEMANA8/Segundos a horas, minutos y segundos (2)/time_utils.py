# Escriba su código aquí
def seconds2hms(segs):
    if segs < 0:
        return 'Tiempo no válido'
    h = int(segs // 3600)
    segs %= 3600
    m = int(segs // 60)
    segs %= 60
    return {'horas': h, 'minutos': m, 'segundos': segs}
