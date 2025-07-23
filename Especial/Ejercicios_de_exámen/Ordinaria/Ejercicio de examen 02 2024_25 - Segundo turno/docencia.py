import re
from auxiliar import show


def verificar(codigo):
    patron = r'^([P-S]{3})[ -]?(\d{5})$'
    coincidencia = re.match(patron, codigo)
    if coincidencia:
        return coincidencia.group(1) + coincidencia.group(2)
    return None


def actualizar(datos_academicos, codigo, notas):
    codigo_verif = verificar(codigo)
    if codigo_verif is None:
        return
    
    asignaturas, estudiantes, calificaciones = datos_academicos
    if codigo_verif not in asignaturas:
        return
    
    if codigo_verif not in calificaciones:
        calificaciones[codigo_verif] = {}
    
    for dni, nota in notas:
        if dni in estudiantes:
            calificaciones[codigo_verif][dni] = nota
    codigo_ok = verificar(codigo)


if __name__ == "__main__":
    datos_académicos = (
        {
            "PQR40953": ("Fundamentos de Programación I", 1, 6),
            "SPP12345": ("Matemáticas", 2, 9),
            "QRP48092": ("Física", 2, 6),
            "RRP45876": ("Redes", 3, 6)
        },
        {
            "40444444X": "Pepito Grillo",
            "40555555Y": "María López",
            "40555566H": "Marta Pérez"
        },
        {
            "PQR40953": {"40444444X": 7.5, "40555555Y": 4.0},
            "SPP12345": {"40444444X": 5.5, "40555555Y": 8.0, "40555566H": 7.0},
            "QRP48092": {},
            "RRP45876": {"40444444X": 5.5, "40555555Y": 3.0, "40555566H": 7.0}
        }
    )
    código = "PQR40953"
    notas = [
        ("40444444X", 8.8), ("40555555Y", 7.5),
        ("40555566H", 9.0), ("25256525G", 6.4)
    ]

    actualizar(datos_académicos, código, notas)
    show(datos_académicos)
