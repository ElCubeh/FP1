# Escriba su código aquí
def show_numbers(num1, num2):
    if num1 > num2:
        num1, num2= num1, num2
    for i in range(num1, num2 + 1):
        print(i)