from auxiliar import show

# Escriba aquí la función


def precio_medio(menú, categoría):

    c = [categoría[0] for categoría in menú]
    if categoría not in c or menú[c.index(categoría)][1] == []:
        return False
    precios = [plato[1] for plato in menú[c.index(categoría)][1]]
    return sum(precios) / len(precios)


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
    show(categorías)
    categoría = input("Introduce el nombre de una categoría:\n")
    pm = precio_medio(menú, categoría)

    if pm:
        print(
            "El precio medio de los platos de '", categoría, "' es:", pm
        )
    else:
        print("La categoría '", categoría, "' no existe.")
