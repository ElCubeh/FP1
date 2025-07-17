# Considérense tuplas, como la del siguiente ejemplo,
#    (
#        {
#            "40953": ("Programación", 1, 6),
#            "40594": ("Matemáticas", 2, 9),
#            "40498": ("Física", 1, 6)
#        },
#        {
#            "40444444X": ("Pepito Grillo", ["40953", "40498"]),
#            "40555555Y": ("María López", ["40953", "40594"])
#        }
#    )
# formadas por dos diccionarios tales que:

# En el primero, cada clave es una string que representa el código de una asignatura, y cada valor asociado, una tupla con el 
# nombre, semestre y número de créditos de aquélla (los semestres son números enteros del 1 al 8; y los créditos pueden tener los 
# valores 3, 6, 9 ó 12).

# El segundo diccionario tiene como claves DNIs y como valores asociados tuplas compuestas por el nombre de un estudiante y una 
# lista con los códigos de las asignaturas en las que está matriculado.

# Escriba una función créditos(datos_académicos, dni) que espere recibir como primer parámetro una tupla con las características 
# mencionadas, y como segundo la string de un DNI. La función devolverá una tupla con el nombre del estudiante al que corresponde 
# el DNI y el número total de créditos en los que está matriculado, salvo que el DNI no se encuentre en el diccionario de 
# estudiantes, en cuyo caso devolverá una tupla con dicho DNI y el número 0. Por ejemplo, si con los datos académicos de la tupla 
# ejemplo preguntamos por el DNI "40444444X", la función deberá devolver la tupla ("Pepito Grillo", 12), pero si preguntamos por 
# el DNI "32458790R", deberá devolver ("32458790R", 0).



# Escriba aquí la función solicitada

def creditos(lista, test):
    materias = lista[0]
    alumnos = lista[1]

    if dni not in alumnos:
        return (dni, 0)
    r = alumnos[dni]
    name, codes = r[0], r[1]

    result =[]
    for code in codes:
        result.append(materias[code][2])
        suma_creditos = sum(result)

    return (name, suma_creditos)



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
