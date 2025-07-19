# Escriba aquí su código
def words_frecs(s):
    word_list = s.split()
    frec_dict = {}
    for word in word_list:
        if word in frec_dict:
            frec_dict[word] += 1
        else:
            frec_dict[word] = 1
    return frec_dict
