import functions

num1 = int(input("Dame un número entero: "))
# Aunque la función acepte que el segundo sea menor, hemos querido pedirle al
# usuario que no lo sea:
num2 = int(input("Dame un otro número entero igual o mayor que el anterior: "))
print(functions.sum_numbers(num1, num2))
