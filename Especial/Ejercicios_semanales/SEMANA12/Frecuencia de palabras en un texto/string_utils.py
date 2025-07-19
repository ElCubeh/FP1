# Escriba aquí su código
import csv
import re

def words_frec(input_file, output_file):
    word_count = {}
    with open(input_file, 'r') as file:
        for line in file:
            words = re.findall(r'\b[a-zA-Z]+\b', line)
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for word, count in sorted(word_count.items()):
                writer.writerow([word, count])
