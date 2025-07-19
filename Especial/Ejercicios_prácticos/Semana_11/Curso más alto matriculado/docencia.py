# Escriba aquí la función solicitada


if __name__ == "__main__":  # Ejemplo de uso
    datos_académicos = (
        {
            "40951": ("Álgebra Y Geometría", 1, 6),
            "40953": ("Fundamentos De Programación I", 1, 6),
            "40957": ("Física", 2, 6),
            "40961": ("Métodos estadísticos", 3, 6),
            "40964": ("Periféricos E Interfaces Obligatoria", 3, 6),
            "40968": ("Bases De Datos I", 4, 6),
            "40973": ("Producción De Software", 6, 9),
            "40990": ("Prácticas Externas", 7, 12),
            "40991": ("Trabajo Fin De Grado", 8, 12),

        },
        {
            "40444444X": ("Pepito Grillo", ["40951", "40961"]),
            "40555555Y": ("María López", ["40968", "40957"]),
            "41444444Z": ("Juan García", ["40973", "40964", "40964"]),
            "40555566A": ("Ana Stasia", []),
            "40355553B": ("Fer Nando", ["40991", "40973"]),
        }
    )
    dni = "40444444X"
    # Deberá devolver ("Pepito Grillo", 2)
    alumno_curso = curso_matriculado(datos_académicos, dni)
    print(f"El estudiante {alumno_curso[0]} está matriculado"
          f" en {alumno_curso[1]}º")
