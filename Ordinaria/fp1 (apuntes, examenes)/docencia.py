# Escriba aquí la función solicitada
def créditos(datos_académicos: tuple, dni: str) -> tuple:
    '''
    Se devolverá, dado un DNI, el nombre del alumno al que pertenece dicho DNI
    y el número de créditos en que está matriculado. En caso de tratarse de un
    DNI que no se encuentre entre los estudiantes, la función devolverá el DNI
    y el número 0.
    '''
    # Separamos la tupla con los datos académicos en asignaturas y alumnos
    # para facilitar el acceso a los datos.
    asignaturas, alumnos = datos_académicos[0], datos_académicos[1]

    if dni in alumnos:
        # En caso de que el DNI se encuentre entre los estudiantes, la variable
        # nombre_alumno hallará su nombre, y la variable número_créditos
        # computará la suma de los créditos en que está matriculado el alumno.
        nombre_alumno = alumnos[dni][0]
        créditos = [asignaturas[código][2] for código in alumnos[dni][1]]
        suma_créditos = sum(créditos)
        return (nombre_alumno, suma_créditos)
    else:
        # En caso de que el DNI no se encuentre entre los estudiantes, se
        # devuelve el DNI y el número 0.
        return (dni, 0)


if __name__ == "__main__":  # Ejemplo de uso
    datos_académicos = (
        {
            "40953": ("Programación", 1, 6),
            "40594": ("Matemáticas", 2, 9),
            "40498": ("Física", 1, 6)
        },
        {
            "40444444X": ("Pepito Grillo", ["40953", "40498"]),
            "40555555Y": ("María López", ["40953", "40594"])
        }
    )

    dni = "40555555Y"
    nombre, total_créditos = créditos(datos_académicos, dni)
    print(
        f"El estudiante '{nombre}' está matriculado",
        f"de un total de {total_créditos} créditos."
    )
