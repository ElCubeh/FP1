import re


# Defina a continuación las dos funciones solicitadas.



if __name__ == "__main__":
    flota = (
        {
            "524967-AB": ("Mercedes", "gasolina", 230),
            "852364-JZ": ("AUDI", "diesel", 200),
            "480925-BM": ("FIAT", "hidrógeno", 120),
            "753951-QT": ("AUDI", "eléctrico", 180),
        },
        {
            "Fuerteventura": ["524967 AB", "852364JZ"],
            "Lanzarote": ["524967AB", "852364-JZ", "480925 BM", "753951-QT"],
            "Tenerife": ["524967-AB", "480925BM", "753951QT"],
            "Gran Canaria": ["524967AB", "480925BM"]
        }
    )
    print(islaCV(flota, "Lanzarote", "AUDI"))
    print(islaCV(flota, "Gran Canaria", "AUDI"))
    print(islaCV(flota, "Mallorca", "AUDI"))
