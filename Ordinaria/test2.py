def creditos(lista, dni):
    asignaturas = lista[0]
    alumnos = lista[1]

    if dni not in alumnos:
        return (dni, 0)
    a = alumnos[dni]
    nombre, codes = a[0], a[1]

    result = []
    for code in codes:
        result.append(asignaturas[code][2])
        suma_creditos = sum(result)
    return (nombre, suma_creditos)

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

    dni = "40444444X"
    nombre, total_créditos = creditos(datos_académicos, dni)
    print(
        f"El estudiante '{nombre}' está matriculado",
        f"de un total de {total_créditos} créditos."
    )
    #print(creditos(datos_académicos, dni))