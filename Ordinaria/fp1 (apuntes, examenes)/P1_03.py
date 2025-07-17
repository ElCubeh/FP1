# Escriba un programa en Python que solicite al usuario ingresar la cantidad de kilómetros recorridos
# por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido para,
# a continuación, mostrar el consumo de combustible por cada 100 kilómetros.

# ==============================================================================================================================

# Ejemplo de ejecución:

# Kilómetros recorridos: 200
# Litros de combustible gastados: 10
# Consumo: 5.0

km = int(input("Kilometros recorridos: "))
litros = int(input("Litros de combustible gastados: "))
consumo = litros/km*100
print(f"Consumo: {consumo}")