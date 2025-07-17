import copy
# Escriba la función solicitada debajo de esta línea

def pmax(imagen):
    result = copy.deepcopy(imagen)
    pmax = 0
    for filas in range(len(result)):
        for pixel in range(len(result[filas])):
            if result[filas][pixel] > pmax and result[filas][pixel] < 255:
                pmax = result[filas][pixel]
    return pmax

def saturated(imagen):
    result = copy.deepcopy(imagen)
    delta = 255 - pmax(imagen)
    for filas in range(len(result)):
        for pixel in range(len(result[filas])):
            result[filas][pixel] += delta
            if result[filas][pixel] > 255:
                result[filas][pixel] = 255
    return result



if __name__ == "__main__":
    """Código para ejecutar la función solicitada."""

    # Cargamos una imagen de ejemplo.
    # Puede cargar otra imagen cambiando get_eii_img() por get_ball_img(size)
    # donde size es un número entero positivo

    # imagen = get_eii_img() NO FUNCIONA

    # Mostramos la imagen original y la resultante del proceso de saturación.
    # cambiando show(imagen) por show(imagen, True) no se muestran los números.
    # (igual show(result, True))

    imagen = [
        [255, 255, 255, 255, 255, 255, 255, 255, 255],
        [255, 0,   0,   0,   255, 128, 255, 176, 255],
        [255, 0,   255, 255, 255, 128, 255, 176, 255],
        [255, 0,   0,   255, 255, 128, 255, 176, 255],
        [255, 0,   255, 255, 255, 128, 255, 176, 255],
        [255, 0,   0,   0,   255, 128, 255, 176, 255],
        [255, 255, 255, 255, 255, 255, 255, 255, 255],
    ]

    # show(imagen) NO FUNCIONA
    print("-" * (5 * len(imagen[0])))
    print(saturated(imagen))