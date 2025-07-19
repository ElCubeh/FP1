# Escriba aquí la función solicitada
def aprobados(datos, cod_asignatura):
    asignaturas, estudiantes, calificaciones = datos
    if cod_asignatura not in calificaciones:
        return []
    calificaciones_asignatura = calificaciones[cod_asignatura]
    estudiantes_aprobados = []
    for dni, calificacion in calificaciones_asignatura.items():
        if calificacion >= 5:
            estudiantes_aprobados.append(estudiantes[dni])
        estudiantes_aprobados.sort()
    return estudiantes_aprobados


if __name__ == "__main__":
    datos_academicos = (
        {
            "40953": ("Fundamentos de Programación I", 1, 6),
            "12345": ("Matemáticas", 2, 9),
            "48092": ("Física", 2, 6),
            "45876": ("Redes", 3, 6)
        },
        {
            "40444444X": "Pepito Grillo",
            "40555555Y": "María López",
            "40555566H": "Marta Pérez"
        },
        {
            "40953": {"40444444X": 7.5, "40555555Y": 4.0},
            "12345": {"40444444X": 5.5, "40555555Y": 8.0, "40555566H": 7.0},
            "45876": {"40444444X": 5.5, "40555555Y": 3.0, "40555566H": 7.0}
        }
    )

    asignatura_codigo = "12345"
    aprobados_asignatura = aprobados(datos_academicos, asignatura_codigo)
    print(
        f"Estudiantes aprobados en la asignatura {asignatura_codigo}:\n",
        "\n".join(aprobados_asignatura),
        sep=""
    )
