# Escriba aquí la función solicitada
"""Escriba una función llamada curso_matriculado(datos_académicos, dni) 
donde dni es el DNI de un estudiante. La función debe devolver una tupla 
con el nombre del estudiante y el número del curso más alto (1, 2, 3 ó 4) 
en el que está matriculado el estudiante. Tenga en cuenta que cada curso se 
compone de dos semestres consecutivos: los semestres 1 y 2 corresponden 
al curso 1, los semestres 3 y 4 al curso 2, y así sucesivamente.

Si el dni no se corresponda con un estudiante, la función debe 
devolver una tupla con el dni pasado como parámetro y el valor None, 
es decir: (dni, None).

En caso de que el estudiante no esté matriculado 
en ninguna asignatura la función debe devolver una tupla con su nombre y 
el valor None, es decir: (nombre del estudiante, None)."""

def curso_matriculado(datos_académicos, dni):
    asignaturas, estudiantes = datos_académicos
    if dni not in estudiantes:
        return (dni, None)
    nombre, cod_asignaturas = estudiantes[dni]
    if not cod_asignaturas:
        return (nombre, None)
    max_curso = 0
    for codigo in cod_asignaturas:
        if codigo in asignaturas:
            semestre = asignaturas[codigo][1]
            max_curso = max(max_curso, (semestre + 1) // 2)
    return (nombre, max_curso)


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
