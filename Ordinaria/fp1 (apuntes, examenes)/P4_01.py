# Teniendo en cuenta que los valores contenidos en una tupla pueden ser de diversos tipos, escriba una función
# cuantos_hay(tupla, tipo) que, siendo tipo un tipo de datos de Python, devuelva el número de elementos de dicho tipo que hay
# en el el parámetro tupla.

# Incluya en el módulo una sección para ejecutar como "__main__" que cree una tupla conteniendo un número entero, dos strings,
# una tupla con cualesquiera tipos de elementos, y un valor booleano; y muestre en pantalla el resultado de llamar a
# cuantos_hay() con los tipos int, str, tuple, bool y float; en ese orden.

# Nota: en textos de informática es usual poner paréntesis vacíos tras el nombre de una función cuando nos referimos a ella
# por su nombre pero no queremos entrar en el detalle de sus parámetros.

def cuantos_hay(tupla, tipo):

    cantidad = 0

    for elemento in tupla:
        if type(elemento) == tipo:
            cantidad +=1
    return cantidad

if __name__ == "__main__":
    tupla_ejem = (7, "lola", "Pro", (6, 8), True, 0.99)
    tipos = (int, str, str, tuple, bool, float)

    for tipo in tipos:
        print(f"Hay", (cuantos_hay(tupla_ejem, tipo)),
        "elmentos de tipo", tipo.__name__, "en tupla.")
