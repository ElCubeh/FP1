"""
Examen: Sistema de Gestión de Estudiantes - Duración máxima: 30 minutos
Contexto:
Imagina que estás desarrollando una pequeña aplicación para gestionar los estudiantes de una escuela. Los estudiantes están organizados en varias clases, y cada clase tiene varios alumnos. Cada alumno tiene un nombre, una lista de notas y una dirección de correo electrónico.

Objetivo:
Debes implementar una serie de funciones que gestionen esta información, validen algunos de los datos e impriman reportes. Todo esto se debe realizar con el uso de tuplas, listas, matrices, expresiones regulares y funciones recursivas.

Parte 1: Estructura de Datos
Define una lista llamada clases, que contendrá varias tuplas, donde cada tupla representa una clase. Cada tupla debe tener dos elementos:

El nombre de la clase (string).
Una lista de estudiantes, donde cada estudiante es también una tupla con los siguientes elementos:
Nombre (string).
Lista de notas (lista de enteros).
Correo electrónico (string).
Ejemplo de una posible entrada:

python
Copiar código
clases = [ ("Matemáticas", [ ("Juan Pérez", [8, 9, 10], "juanp@correo.com"), ("Ana Gómez", [6, 7, 8], "anag@correo.com") ]), ("Ciencias", [ ("Carlos Ruiz", [7, 8, 9], "carlosr@correo.com"), ("Marta Sánchez", [9, 10, 9], "martas@correo.com") ]) ]
Parte 2: Función de Promedio de Notas
Crea una función llamada calcular_promedio que reciba una lista de notas (enteros) y devuelva el promedio de las notas. Si la lista está vacía, devuelve None.
Parte 3: Validación de Correo Electrónico
Crea una función llamada es_correo_valido que reciba una dirección de correo electrónico y valide que siga este patrón básico: algo@dominio.com. Utiliza expresiones regulares para hacer la validación. La función debe devolver True si el correo es válido y False en caso contrario.
Parte 4: Generación de Reportes
Crea una función llamada generar_reporte que reciba la lista clases y devuelva un reporte con la siguiente información:
El nombre de cada clase.
El nombre de cada estudiante y su promedio de notas (utiliza la función calcular_promedio).
Si el correo electrónico del estudiante es válido (utiliza la función es_correo_valido), imprime "Correo válido", de lo contrario imprime "Correo no válido".
Parte 5: Función Recursiva para Buscar Estudiantes por Nombre
Crea una función recursiva llamada buscar_estudiante que reciba el nombre de un estudiante y la lista clases. La función debe buscar al estudiante en todas las clases (en cada lista de estudiantes) y devolver la primera clase en la que se encuentra el estudiante, junto con su promedio de notas. Si no se encuentra al estudiante, debe devolver None.
Puntos a Tener en Cuenta:
Tuplas: Se utilizan para almacenar la información inmutable de las clases y los estudiantes.
Listas: Se usan para almacenar los estudiantes y sus notas.
Matrices (listas de listas): Utiliza una lista de listas para representar las clases y los estudiantes.
Expresiones Regulares: Se deben usar para validar el formato de los correos electrónicos.
Funciones Recursivas: La función buscar_estudiante debe implementarse de forma recursiva.
Ejemplo de salida esperada:
Supongamos que la lista clases es como la del ejemplo inicial. Al ejecutar la función generar_reporte, podrías obtener algo como esto:

yaml
Copiar código
Clase: Matemáticas Estudiante: Juan Pérez, Promedio: 9.0, Correo válido Estudiante: Ana Gómez, Promedio: 7.0, Correo válido Clase: Ciencias Estudiante: Carlos Ruiz, Promedio: 8.0, Correo válido Estudiante: Marta Sánchez, Promedio: 9.33, Correo válido
Si se busca un estudiante llamado "Carlos Ruiz", la función buscar_estudiante debería devolver algo como:

yaml
Copiar código
Carlos Ruiz encontrado en la clase: Ciencias, Promedio: 8.0
Instrucciones finales:
Tienes 30 minutos para completar el examen.
Asegúrate de que el código sea legible y esté bien organizado.
Verifica que cada función esté correctamente implementada y que no haya errores de sintaxis.
Este ejercicio te permite demostrar tus habilidades trabajando con estructuras de datos (tuplas, listas, matrices), validando datos con expresiones regulares y utilizando recursión de manera eficiente. ¡Mucho éxito!

4o mini
 
Tú dijiste:
como saber si una cadena sigue un patron de expresiones regulares
ChatGPT Plus
ChatGPT
Para verificar si una cadena sigue un patrón de expresión regular en Python, puedes usar el módulo re, que proporciona funciones para trabajar con expresiones regulares. La función principal que puedes usar para verificar si una cadena coincide con un patrón es re.match(), re.fullmatch() o re.search(). Aquí te explico cómo funcionan y cuándo usarlas:

1. re.match():
Verifica si el patrón coincide al principio de la cadena. Si la coincidencia es exitosa, devuelve un objeto de coincidencia; si no, devuelve None.

python
Copiar código
import re # Patrón de expresión regular patron = r"\d{3}" # Un patrón que verifica tres dígitos consecutivos # Cadena de prueba cadena = "123abc" # Verifica si el patrón coincide al inicio coincidencia = re.match(patron, cadena) if coincidencia: print("Coincidencia encontrada:", coincidencia.group()) else: print("No se encontró coincidencia")
En este caso, la salida será:

yaml
Copiar código
Coincidencia encontrada: 123
2. re.fullmatch():
Verifica si toda la cadena coincide completamente con el patrón. Si la cadena cumple con todo el patrón, devuelve un objeto de coincidencia; si no, devuelve None.

python
Copiar código
import re # Patrón de expresión regular patron = r"\d{3}" # Un patrón que verifica tres dígitos # Cadena de prueba cadena = "123" # Verifica si toda la cadena coincide con el patrón coincidencia = re.fullmatch(patron, cadena) if coincidencia: print("Coincidencia completa encontrada:", coincidencia.group()) else: print("No se encontró coincidencia completa")
En este caso, la salida será:

yaml
Copiar código
Coincidencia completa encontrada: 123
Si la cadena fuera "123abc", la salida sería:

yaml
Copiar código
No se encontró coincidencia completa
"""

import re

# Parte 1: Estructura de Datos
clases = [
    ("Matemáticas", [
        ("Juan Pérez", [8, 9, 10], "juanp@correo.com"),
        ("Ana Gómez", [6, 7, 8], "anag@correo.com")
    ]),
    ("Ciencias", [
        ("Carlos Ruiz", [7, 8, 9], "carlosr@correo.com"),
        ("Marta Sánchez", [9, 10, 9], "martas@correo.com")
    ])
]

# Parte 2: Función de Promedio de Notas
def calcular_promedio(notas):
    if not notas:
        return None
    return sum(notas) / len(notas)

# Parte 3: Validación de Correo Electrónico
def es_correo_valido(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(patron, correo) is not None

# Parte 4: Generación de Reportes
def generar_reporte(clases):
    reporte = []
    for clase, estudiantes in clases:
        reporte.append(f"Clase: {clase}")
        for estudiante in estudiantes:
            nombre, notas, correo = estudiante
            promedio = calcular_promedio(notas)
            correo_valido = "Correo válido" if es_correo_valido(correo) else "Correo no válido"
            reporte.append(f"Estudiante: {nombre}, Promedio: {promedio:.2f}, {correo_valido}")
    return "\n".join(reporte)

# Parte 5: Función Recursiva para Buscar Estudiantes por Nombre
def buscar_estudiante(nombre, clases):
    for clase, estudiantes in clases:
        for estudiante in estudiantes:
            if estudiante[0] == nombre:
                promedio = calcular_promedio(estudiante[1])
                return f"{nombre} encontrado en la clase: {clase}, Promedio: {promedio:.2f}"
    return None

# Ejemplo de uso
if __name__ == "__main__":
    print(generar_reporte(clases))
    resultado_busqueda = buscar_estudiante("Carlos Ruiz", clases)
    if resultado_busqueda:
        print(resultado_busqueda)
    else:
        print("Estudiante no encontrado.")