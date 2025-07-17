# Escriba la función solicitada debajo de esta línea

def aclarar(imagen, magnitud):

    if (magnitud <= 0 or magnitud >= 100):
        return "Magnitude out of range"
    else:
        for filas in range(len(imagen)):
            for elemento in range(len(imagen[filas])):
                if (imagen[filas][elemento] + magnitud) > 255:
                    imagen[filas][elemento] = 255
                else:
                    imagen[filas][elemento] += magnitud
        return "Process finished"

if __name__ == "__main__":
    """Código para ejecutar la función solicitada."""

    imagen = [
        [255, 255, 255, 255, 255, 255, 255, 255, 255],
        [255, 0,   0,   0,   255, 128, 255, 176, 255],
        [255, 0,   255, 255, 255, 128, 255, 176, 255],
        [255, 0,   0,   255, 255, 128, 255, 176, 255],
        [255, 0,   255, 255, 255, 128, 255, 176, 255],
        [255, 0,   0,   0,   255, 128, 255, 176, 255],
        [255, 255, 255, 255, 255, 255, 255, 255, 255],
    ]

    magnitud = 50

    print(aclarar(imagen, magnitud))
