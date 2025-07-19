# Escriba su código aquí
def seconds2hms(segundos):
    horas = segundos // 3600
    segundos = segundos - horas * 3600
    minutos = segundos // 60
    segundos = segundos - minutos * 60
    return (horas, minutos, segundos)
    