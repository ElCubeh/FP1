from auxiliar import *

# Escriba la función systolic_pressure_risk debajo de esta línea



if __name__ == "__main__":
    """Código para ejecutar la función solicitada."""

    # Un caso de prueba con solo dos semanas

    weekly_readings = [
        [   # Week 1
            (75, 110), (80, 115), (78, 118), (77, 116),
            (76, 117), (79, 110), (74, 112)
        ],
        [   # Week 2
            (76, 111), (75, 115), (78, 119), (77, 114),
            (80, 113), (79, 112), (78, 110)
        ]
    ]

    # Llamada a la función

    risk = systolic_pressure_risk(weekly_readings)

    # Mostramos el resultado

    print("El riesgo calculado es:", risk)
