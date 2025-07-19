import functions

if __name__ == "__main__":
    print("Se va arealizar una división entera")
    dividendo = int(input("Dame el dividendo: "))
    divisor = int(input("Dame el divisor: "))
    result = functions.division(dividendo, divisor)
    print(result)
