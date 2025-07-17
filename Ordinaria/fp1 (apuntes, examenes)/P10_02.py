# Considérense tuplas cada una conteniendo tres diccionarios:

# Cada uno de los componentes del primero tiene como clave una string con un código de asignatura; y como valor una tupla con su
# nombre, su semestre y su número de créditos. Los semestres se codifican con un número entero del 1 al 8; y los créditos pueden
# tener los valores 3, 6, 9 ó 12.

# El segundo diccionario usa como clave una string con un DNI de estudiante y como valor una string con su nombre.

# El tercer diccionario usa como clave un código de asignatura y como valor un diccionario, el cual a su vez usa como clave una
# string con un DNI y como valor un número entre cero y diez que representa la calificación obtenida por ese estudiante en esa
# asignatura. No incluye asignaturas sin calificaciones.

# Ver ejemplo en el código suministrado:

# Escriba una función aprobados(datos, cod_asignatura) que devuelva una lista ordenada alfabéticamente con los nombres de los
# estudiantes que han aprobado la asignatura cuyo código está indicado por el segundo parámetro. El primer parámetro de la función
# es una tupla de datos académicos como se ha descrito. Un estudiante aprueba una asignatura si su calificación es de cinco, al
# menos.

# Escriba aquí la función solicitada

def aprobados(lista, codigo):
    a = []
    for asignatura, dni_nota in lista[2].items():
        if codigo == asignatura:
            for dni, nota in lista[2][asignatura].items():
                if nota >= 5:
                    a.append(lista[1][dni])
    a.sort()
    return(a)




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
