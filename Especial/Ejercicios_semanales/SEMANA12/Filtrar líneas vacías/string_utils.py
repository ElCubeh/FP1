# Escriba aquí su código
def no_empty_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    with open(output_file, 'w') as f:
        for line in lines:
            if not line.isspace():
                f.write(line)
