# Escriba aquí su código
def format_frecs(frecs_total):
    word_dict, total_words = frecs_total
    result = []
    for word, freq in word_dict.items():
        rel_freq = round((freq / total_words) * 100, 2)
        result.append(f"{word:<10}:{rel_freq:.2f}%")
    return result
