# Se tiene un diccionario cuyas claves son nombres de frutas (tipo str) y cuyos valores son números que representan el precio por
# kilo de la fruta identificada por la clave. Una fruta, temporalmente, puede no estar disponible, en cuyo caso tendrá asociado el
# valor -1. Ver el código de ejemplo.

# Parte 1: Escriba una función, precio_kilos(precios, fruta, kilos), donde precios es un diccionario como el descrito, fruta es el
# nombre de una fruta, y kilos es un número que expresa una cantidad en kilos de dicha fruta. La función debe devolver el coste de
# esa cantidad de kilos de esa fruta. En caso de que la fruta no esté en el diccionario precios o, temporalmente, no esté
# disponible, la función devolverá el valor None.

# Parte 2: Escriba una función, mensaje_precio_kilos(precios, fruta, kilos), que, usando la función anterior, devuelva una string
# con el siguiente formato:

"<k> kilos de '<fruta>' cuestan <coste> euros"

#donde <k> es el número de kilos, <fruta> es el nombre de la fruta y <coste> es el coste total de esos kilos de fruta calculado por
# la función anterior, que se mostrará como número float con dos dígitos decimales:

"3 kilos de 'pera' cuestan 9.00 euros"

# En el caso de que la fruta no esté en el diccionario precios o, temporalmente, no esté disponible, el mensaje será: 

"La fruta '<fruta>' no está disponible."

# como en: "La fruta 'kiwi' no está disponible." o "La fruta 'uva' no está disponible."

# Escriba aquí su código

def precio_kilos(lista, fruta, kilos):
    for frutas in lista:
        if fruta == frutas:
            if lista[frutas] >= 0:
                return lista[frutas]*kilos
    return None

def mensaje_precio_kilos(lista, fruta, kilos):
    for frutas in lista:
        if fruta == frutas:
            if lista[frutas] >= 0:
                return f"{kilos} kilos de '{fruta}' cuestan {lista[frutas]*kilos} euros"
    return f"La fruta '{fruta}' no está disponible."


if __name__ == "__main__":
    precios_frutas = {
        "manzana": 2.5,
        "pera": 3.0,
        "banana": 1.8,
        "uva": -1  # Fruta no disponible temporalmente
    }

    fruta = "manzana"
    kilos = 3
    costo_total = precio_kilos(precios_frutas, fruta, kilos)
    print(costo_total)
    
    mensaje = mensaje_precio_kilos(precios_frutas, fruta, kilos)
    print(mensaje)
