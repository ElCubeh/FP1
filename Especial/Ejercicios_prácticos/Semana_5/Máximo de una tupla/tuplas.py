def máximo(tupla):
    max_valor = tupla[0]
    for valor in tupla:
        if valor > max_valor:
            max_valor = valor
    return max_valor


if __name__ == "__main__":
    valores = (5, 10, 2, 8, 3)
    resultado = máximo(valores)
    print(resultado)
