def factorial(n):
    resultado = 1
    if n < 0:
        return None
    else:
        for i in range(1,n+1):
            resultado *= i
    return resultado