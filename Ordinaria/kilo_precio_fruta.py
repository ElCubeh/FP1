"""Se tiene un diccionario cuyas claves son nombres de frutas (tipo str) y cuyos valores son números que representan el precio por kilo de la fruta identificada por la clave. Una fruta, temporalmente, puede no estar disponible, en cuyo caso tendrá asociado el valor -1. Por ejemplo:

precios_frutas = {
    "manzana": 2.5,
    "pera"   : 3.0,
    "plátano": 1.8,
    "uva"    : -1  # Fruta no disponible temporalmente
}
Parte 1: Escriba una función, precio_kilos(precios, fruta, kilos), donde precios es un diccionario como el descrito, fruta es el nombre de una fruta, y kilos es un número que expresa una cantidad en kilos de dicha fruta. La función debe devolver el coste de esa cantidad de kilos de esa fruta. En caso de que la fruta no esté en el diccionario precios o, temporalmente, no esté disponible, la función devolverá el valor None.

Parte 2: Escriba una función, mensaje_precio_kilos(precios, fruta, kilos), que, usando la función anterior, devuelva una string con el siguiente formato:

"<k> kilos de '<fruta>' cuestan <coste> euros"

donde <k> es el número de kilos, <fruta> es el nombre de la fruta y <coste> es el coste total de esos kilos de fruta calculado por la función anterior, que se mostrará como número float con dos dígitos decimales:

"3 kilos de 'pera' cuestan 9.00 euros"

En el caso de que la fruta no esté en el diccionario precios o, temporalmente, no esté disponible, el mensaje será: 

"La fruta '<fruta>' no está disponible."

como en: "La fruta 'kiwi' no está disponible." o "La fruta 'uva' no está disponible."""



def precio_kilos(precios, fruta, kilos):
    if fruta not in precios or precios[fruta] == -1:
        return None
    return precios[fruta] * kilos


def mensaje_precio_kilos(precios, fruta, kilos):
    costo = precio_kilos(precios, fruta, kilos)
    if costo is None:
        return f"La fruta '{fruta}' no está disponible."
    return f"{kilos} kilos de '{fruta}' cuestan {costo:.2f} euros"


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
    # Descomentar esta parte cuando esté hecha la segunda función
    mensaje = mensaje_precio_kilos(precios_frutas, fruta, kilos)
    print(mensaje)