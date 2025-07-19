# Escriba su código aquí
def transform_date(date):
    dia = date[0:2]
    mes = date[3:5]
    año = date[6:]
    fecha_nueva = mes + '-' + dia + '-' + año
    return  fecha_nueva