# El menú de un restaurante se ha almacenado en una estructura de datos de Python con las siguientes características:

# La estructura es una lista.

# Cada elemento de la lista es una tupla de dos elementos.

# El primer elemento de esta tupla es una string que representa el nombre de una categoría de platos,
# por ejemplo: "Entrantes calientes", "Entrantes fríos", "De cuchara", …

# El segundo elemento de la tupla es una lista de tuplas

# El primer elemento de cada una de estas tuplas es el nombre de un plato.

# El segundo elemento es el precio del plato, representado como un número real, por ejemplo: ("Papas arrugadas", 8.50)

# No hay nombres de platos repetidos ni en la misma ni en distintas categorías.

# Ejemplo:

#     menú = [
#         ("Entrantes calientes", [
#             ("Sopa de tomate", 4.50),
#             ("Croquetas de jamón", 6.50),
#             ("Calamares a la romana", 9.50)
#          ]),
#         ("Entrantes fríos", [
#             ("Ensalada César", 7.50),
#             ("Gazpacho", 5.00),
#             ("Carpaccio de salmón", 10.00)
#          ]),
#         ("De cuchara", [
#             ("Lentejas", 6.00),
#             ("Sopa de mariscos", 9.00),
#             ("Crema de calabaza", 5.50)
#         ])
#     ]
# Escriba una función, precio_medio(menú, nombre_categoría), en la que menú es una lista de categorías como la descrita
# y nombre_categoría es el nombre de la categoría a seleccionar. La función debe devolver el precio medio de los platos
# de la categoría especificada; en caso de que la categoría no exista en el menú o no tenga platos, deberá devolver False.


def precio_medio(menu, categoria):
    precio_total = 0
    for cate, platos in menu:
        if categoria == cate:
            precio_total = sum(j for i, j in platos)
            return precio_total / len(platos)
    return False



if __name__ == "__main__":
    menú = [
        ("Entrantes calientes", [
            ("Sopa de tomate", 4.50),
            ("Croquetas de jamón", 6.50),
            ("Calamares a la romana", 9.50)
        ]),
        ("Entrantes fríos", [
            ("Ensalada César", 7.50),
            ("Gazpacho", 5.00),
            ("Carpaccio de salmón", 10.00)
        ]),
        ("De cuchara", [
            ("Lentejas", 6.00),
            ("Sopa de mariscos", 9.00),
            ("Crema de calabaza", 5.50)
        ])
    ]
    categorías = [item[0] for item in menú]
    categoría = input("Introduce el nombre de una categoría:\n")
    pm = precio_medio(menú, categoría)

    if pm:
        print(
            "El precio medio de los platos de '", categoría, "' es:", pm
        )
    else:
        print("La categoría '", categoría, "' no existe.")