# Escriba su código aquí
def house_position(houses_lista, target_piso):
    try:
        return houses_lista.index(target_piso)
    except ValueError:
        return None
