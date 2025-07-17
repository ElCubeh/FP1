import re
from auxiliar import show


def verificar(código):
    """Desarrollar esta función de manera adecuada"""
    """Si no la desarrolla, la nota máxima que podrá obtener será 8"""

    return código


def actualizar(datos_académicos, código, notas):
    """Completar esta función de manera adecuada"""

    códigoOk = verificar(código)


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
