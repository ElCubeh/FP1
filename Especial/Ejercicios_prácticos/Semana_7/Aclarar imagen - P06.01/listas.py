from auxiliar import *


# Escriba la función solicitada debajo de esta línea
def aclarar(imagen, magnitud):
    if magnitud < 0 or magnitud > 100:
        return "Magnitude out of range"
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            new_value = imagen[i][j] + magnitud
            if new_value > 255:
                new_value = 255
            imagen[i][j] = new_value
    return "Process finished"


if __name__ == "__main__":
    """Código para ejecutar la función solicitada."""

    # Cargamos una imagen de ejemplo:
    imagen = get_eii_img()
    # Puede cargar otra imagen con get_ball_img(size),
    # donde size es un número entero entre 7 y 15.

    # Mostramos la imagen original y la resultante del proceso
    # (usando show(imagen, True) no se mostrarían los números).
    magnitud = 50
    show(imagen)
    print(aclarar(imagen, magnitud))
    show(imagen)
