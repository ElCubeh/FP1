def tipo_renta(euro):
    if euro <= 10000:
        print(5)
    if 10000 >= euro <= 20000:
        print(15)
    elif 20000 >= euro <= 35000:
        print(20)
    elif 35000 >= euro <= 60000:
        print(30)
    elif 60000 <= euro:
        print(45)
