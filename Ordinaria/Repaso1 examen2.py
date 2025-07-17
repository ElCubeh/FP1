"""Considera la siguiente estructura de datos:

(
    {
        "40953": ("Programación", 1, 6),
        "40594": ("Matemáticas", 2, 9),
        "40498": ("Física", 1, 6),
        "40876": ("Química", 2, 3)
    },
    {
        "40444444X": ("Pepito Grillo", [("40953", 8), ("40498", 6)]),
        "40555555Y": ("María López", [("40953", 5), ("40594", 7), ("40876", 3)])
    }
)

La estructura es similar a la anterior, pero en este caso, la lista asociada a cada estudiante contiene tuplas con el código de la asignatura y la nota que ha obtenido en dicha asignatura.

Escribe una función promedio_estudiante(datos_académicos, dni) que reciba como primer parámetro una tupla con la estructura de datos anterior y como segundo parámetro el DNI de un estudiante. La función debe devolver una tupla con el nombre del estudiante y su promedio ponderado en base a los créditos de cada asignatura. Si el estudiante no se encuentra en el diccionario, debe devolver una tupla con el DNI y el número 0.
Ejemplos de salida:

    Si se llama a la función con el DNI "40444444X", debe devolver ("Pepito Grillo", 7.0), considerando que Pepito cursa 12 créditos y obtiene un promedio ponderado.

    Si se llama a la función con el DNI "32458790R", debe devolver ("32458790R", 0) porque el DNI no está registrado
"""
def promedio_estudiante(lista, dni):
    asignaturas = lista[0]
    alumnos = lista[1]
    if dni not in alumnos:
        return (dni, 0)
    nombre, codes= alumnos[dni]

    nota_promedio = 0
    result = 0
    for code, nota in codes:
        if code in asignaturas:
            creditos = asignaturas[code][1]
            result += creditos
            nota_promedio += nota * creditos
    if result == 0:
        return (nombre, 0)
    
    promedio_ponderado = round(nota_promedio / result, 2)
    
    return (nombre, promedio_ponderado) 


if __name__ == "__main__":
    datos_academicos = (
        {
            "40953": ("Programación", 1, 6),
            "40594": ("Matemáticas", 2, 9),
            "40498": ("Física", 1, 6),
            "40876": ("Química", 2, 3)
        },
        {
            "40444444X": ("Pepito Grillo", [("40953", 8), ("40498", 6)]),
            "40555555Y": ("María López", [("40953", 5), ("40594", 7), ("40876", 3)])
        }
    )

    dni_list = ["40444444X", "40555555Y", "32458790R"]

    for dni in dni_list:
        resultado = promedio_estudiante(datos_academicos, dni)
        print(f"DNI: {dni} -> Resultado: {resultado}")