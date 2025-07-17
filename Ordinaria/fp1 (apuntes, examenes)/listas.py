from auxiliar import *
import copy

# Escriba la función solicitada debajo de esta línea


# Creación de función auxiliar para calcular pmax
def calculo_pmax(imagen):
    pmax = 0
    for row in range(len(imagen)):
        # La variable maximum almacenará la mayor cantidad,
        # por fila, estrictamente inferior a 255
        maximum = 0
        for pixel in range(len(imagen[row])):
            if maximum < imagen[row][pixel] < 255:
                maximum = imagen[row][pixel]
        # La variable pmax almacenará el mayor de los resultados
        # parciales de maximum
        if maximum > pmax:
            pmax = maximum
    return pmax


def saturated(imagen):
    # Inicialización: copia de la imagen (la función no modifica la original)
    result = copy.deepcopy(imagen)
    # Cálculo de pmax con la función creada para ello
    pmax = calculo_pmax(result)
    # Cálculo de delta
    delta = 255 - pmax
    # Realizar la saturación
    for row in range(len(result)):
        for pixel in range(len(result[row])):
            result[row][pixel] += delta
            # Poner a 255 los valores que superen dicha cantidad
            if result[row][pixel] > 255:
                result[row][pixel] = 255
    # Devolver la imagen saturada
    return result


if __name__ == "__main__":
    """Código para ejecutar la función solicitada."""

    # Cargamos una imagen de ejemplo.
    # Puede cargar otra imagen cambiando get_eii_img() por get_ball_img(size)
    # donde size es un número entero positivo

    imagen = get_eii_img()

    # Mostramos la imagen original y la resultante del proceso de saturación.
    # cambiando show(imagen) por show(imagen, True) no se muestran los números.
    # (igual show(result, True))

    show(imagen)
    result = saturated(imagen)
    print("-" * (5 * len(imagen[0])))
    show(result)
