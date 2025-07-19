# Escriba aquí su código
def extraer_nums(lista):
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(extraer_nums(elemento))
        elif isinstance(elemento, int):
            resultado.append(elemento)
    return resultado


if __name__ == "__main__":
    lista_de_prueba = [
        35, 14,
        [
            [12, 34],
            14, 98,
        ],
        10, 12, 28,
        [
            56,
            [
                [10, 14],
                [11]
            ]
        ]
    ]
    print(extraer_nums(lista_de_prueba))
