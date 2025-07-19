# Escriba aquí su código
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
    """
    # Descomentar esta parte cuando esté hecha la segunda función
    mensaje = mensaje_precio_kilos(precios_frutas, fruta, kilos)
    print(mensaje)
    """
