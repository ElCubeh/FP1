#Se tiene una tupla de datos académicos formada por dos diccionarios:

# El primero tiene como claves, strings que representan códigos de asignaturas, y como valores, tuplas, con el nombre, semestre y
# número de créditos de ésta. Por ejemplo: {"40953": ("Fundamentos de Programación I", 1, 6)}. Los semestres son números enteros
# de 1 a 8 y los créditos pueden tener los valores 3, 6, 9 o 12.

# El segundo diccionario tiene como claves, DNIs y como valores, tuplas compuestas por el nombre de un estudiante y una lista con
# los códigos de las asignaturas en las que está matriculado.

# Ejemplo:

#    datos_académicos = (
#        {
#            "40953": ("Programación", 1, 6),
#            "40594": ("Matemáticas", 2, 9),
#            "40498": ("Física", 1, 6)
#        },
#        {
#            "40444444X": ("Pepito Grillo", ["40953", "40498"]),
#            "40555555Y": ("María López", ["40953", "40594"]),
#            "41444444Z": ("Juan García", ["40953", "40594"]),
#            "40555566A": ("Ana Stasia", ["40498"]),
#            "40355553B": ("Fer Nando", ["40594"])
#        }
#    )

# Escriba una función, matriculados(datos_académicos, código_asignatura, dnis), donde código_asignatura es un código de asignatura
# y dnis es una lista de dnis. La función debe devolver una tupla con el nombre de la asignatura correspondiente al código y un
# número indicando cuántos de los dnis de la lista corresponden a estudiantes matriculados en tal asignatura. En caso de que la
# asignatura indicada en el código no figure en los datos, la función debe devolver None.



# Escriba aquí la función solicitada

def matriculados(lista, código, dnis):
    asignaturas = lista[0]
    alumnos = lista[1]

    if código not in asignaturas:
        return None
    asignatura = asignaturas[código][0]

    cuenta = 0
    for dni in dnis:
        if dni in alumnos and código in alumnos[dni][1]:
            cuenta += 1
    return (asignatura, cuenta)

if __name__ == "__main__":  # Ejemplo de uso
    datos_académicos = (
        {
            "40953": ("Programación", 1, 6),
            "40594": ("Matemáticas", 2, 9),
            "40498": ("Física", 1, 6)
        },
        {
            "40444444X": ("Pepito Grillo", ["40953", "40498"]),
            "40555555Y": ("María López", ["40953", "40594"]),
            "41444444Z": ("Juan García", ["40953", "40594"]),
            "40555566A": ("Ana Stasia", ["40498"]),
            "40355553B": ("Fer Nando", ["40594"])
        }
    )

    código = "40953"
    dnis = ["40444444X", "40555555Y", "40555566A"]
# Deberá devolver ("Programación", 2)
    cuenta_matricula = matriculados(datos_académicos, código, dnis)
    if cuenta_matricula:
        print(
            f"{cuenta_matricula[1]} de los estudiantes consultados",
            f"están matriculados en la asignatura '{cuenta_matricula[0]}'",
        )
    else:
        print(f"No existe una asignatura con el código '{código}'")