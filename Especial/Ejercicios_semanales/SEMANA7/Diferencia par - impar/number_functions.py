# Escriba aquí su código
def dif_par_impar(lista1, lista2):
    suma_par = 0
    suma_impar = 0
    for i in range(len(lista1)):
        if (lista1[i] + lista2[i]) % 2 == 0:
            suma_par += 1
        else:
            suma_impar += 1
    return (suma_par, suma_impar)
