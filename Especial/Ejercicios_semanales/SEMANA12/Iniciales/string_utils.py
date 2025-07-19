# Escriba aquí su código
def save_initials(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            words = line.split()
            initials = ' '.join([word[0] for word in words])
            f.write(initials + '\n')
