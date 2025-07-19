def inicial_o_final(primer_texto, segundo_texto):
    if primer_texto[0] == segundo_texto[0]:
        return True
    elif primer_texto[-1] == segundo_texto[-1]:
        return True
    else:
        return False
