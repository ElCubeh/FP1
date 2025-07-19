# Escriba su código aquí
def format_pows(n, fill_char=' '):
    number_str = str(n).zfill(2)
    square_str = str(n**2).zfill(3)
    cube_str = str(n**3).zfill(4)
    result = f"{number_str}{square_str}{cube_str}"
    return result
