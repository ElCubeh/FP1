def dice_freqs(lista):
    freqs = [0]*6
    for tirada_dado in lista:
        for numero in tirada_dado:
            freqs[num-1] += 1
    return freqs
