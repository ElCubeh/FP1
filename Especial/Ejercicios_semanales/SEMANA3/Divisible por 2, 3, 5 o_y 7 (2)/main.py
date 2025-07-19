numero = int(input("Dame un valor entero: "))
divisores = []
if numero %2 ==0:
    divisores.append(2)
if numero %3 ==0:
    divisores.append(3)
if numero %5 ==0:
    divisores.append(5)
if numero %7 ==0:
    divisores.append(7)
if len(divisores) == 0:
    pass
elif len(divisores) == 1:
    print(divisores[0])
else:
    divisores.sort()
    for divisor in divisores:
        print(divisor)