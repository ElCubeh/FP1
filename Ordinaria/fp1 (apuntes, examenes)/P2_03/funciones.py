def tipo_renta(euros):
    if euros < 10000:
        return 5
    elif euros >= 10000 and euros < 20000:
        return 15
    elif euros >= 20000 and euros < 35000:
        return 20
    elif euros >= 35000 and euros < 60000:
        return 30
    elif euros >= 60000:
        return 45