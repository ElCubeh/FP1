# -*- coding: utf-8 -*-

#Práctica 2 VIU
#1. Suma de primos
def es_primo(n):
    """Encuentra si un número natural > 1 es primo o no
    >>> es_primo(57)
    False
    >>> es_primo(59)
    True
    """
    for d in range(2, n//2+1):
        if n % d == 0:       # Se busca algún divisor
            return False
    return True

def suma_primos(N):
    """
    llama a es_primo(n) y calcula la suma de numeros primos entre 2 y n, sin incluir n
    >>> suma_primos(5)
    5
    >>> suma_primos(9)
    17
    >>> suma_primos(39)
    197
    >>> suma_primos(100)
    1060
    """
    suma = 0 # Inicializamos la suma
    for i in range(2, N): # Recorre los números desde el 2 hasta N-1
        if es_primo(i): # Si el parámetro de la función es i
            suma += i # Sumar la posición i a la suma
    return suma # Devuelve la suma


# Comprobamos los resultados mostrándolos en pantalla
print(suma_primos(5))
print(suma_primos(9))
print(suma_primos(39))
print(suma_primos(100))


"""
 2. Serie alternada   (a)
"""
def serieLn(n):
    """ Calcula la sumatoria de la serie alternada, dado el número de términos n
    >>> serieLn(4)
    0.58333333
    >>> serieLn(10)
    0.64563492
    >>> serieLn(1000)
    0.69264743
    >>> serieLn(1000000)
    0.69314668
    """
    sumatoria = 0 # Se inicializa la sumatoria
    for i in range(1, n+1): # Recorre desde los números 1 hasta n
        termino = (-1)**(i+1) / i # Calcula el término actual de la serie
        sumatoria += termino # Suma el término a la sumatoria
    return round(sumatoria, 8) # Se redondea el resultado a 8 decimales y se devuelve


# Comprobación de resultados mostrándolos en pantalla
print(serieLn(4))
print(serieLn(10))
print(serieLn(1000))
print(serieLn(1000000))


# (b)
def serieLn2(eps):
    """ Calcula la sumatoria de la serie alternada mientras termino > eps
    >>> serieLn2(0.1)
    0.64563492
    >>> serieLn2(0.001)
    0.69264743
    >>> serieLn2(0.000001)
    0.69314668
    """
    # Establecemos las variables necesarias
    sumatoria = 0 # Inicializamos la sumatoria
    i = 1 # Establecemos la primera posición como 1
    termino = (-1)**(i + 1) / i # Defiminos el término actual
    while termino > eps: # Mientras el término sea mayor que epsilon:
        sumatoria += termino # A sumatoria se le suma el término
        i += 1 # Se incrementa 1 posición
    return round(sumatoria, 8) # Redondeamos a 8 decimales y devolvemos sumatoria


# Comprobación de resultados mostrándolos en pantalla
print(serieLn2(0.1))
print(serieLn2(0.001))
print(serieLn2(0.000001))


# Análisis con logaritmo natural de 2
import math


ln2 = math.log(2)
# Mediante el formateo de strings mostramos en pantalla los resultados pudiendo así analizarlos
print(f"Logaritmo natural de 2: {ln2:.8f}")
print(f"SerieLn(1000000): {serieLn(1000000):.8f}")
print(f"SerieLn2(0.000001): {serieLn2(0.000001):.8f}")


"""
 3. Suma de divisores propios
"""
def sumaDivProp(n):
    """ Suma divisores excepto él mismo
    >>> sumaDivProp(10)
    8
    >>> sumaDivProp(4)
    3
    >>> sumaDivProp(28)
    28
    >>> sumaDivProp(220)
    284
    """
    suma = 0 # Inicializa la suma
    for i in range(1, n): # Recorre desde los números 1 hasta n-1
        if n % i == 0: # Si i es divisor de n
            suma += i # Se suma el divisor propio a la suma
    return suma # Devuelve la suma total de los divisores


# Comprobamos los resultados mostrándolos en pantalla
print(sumaDivProp(10))
print(sumaDivProp(4))
print(sumaDivProp(28))
print(sumaDivProp(220))


""" 
  4. Número perfecto
"""
def perfecto(ini=28):
    """ Buscar el número perfecto a partir de n (ejemplo n=28)
    >>> perfecto(1)
    6
    >>> perfecto(6)
    28
    >>> perfecto(28)
    496
    >>> perfecto(500)
    8128
    """
    for i in range(ini+1, 8128): # Iterar a partir de ini sin exceder el número 8128
        if i == sumaDivProp(i): # Si la suma de los divisores propios es igual al número i actual
            return i # Devuelve el número perfecto, i


# Comprobamos los resultados mostrándolos en pantalla
print(perfecto(1))
print(perfecto(6))
print(perfecto(28))
print(perfecto(500))


"""
 5. Integral definida de f(x) = 3 + x**3 entre a y b
"""
def integral_definida(a,b):
    """ Integral definida de f(x) = 3+x**3 entre x=a y x=b, aproximada por
    el método de integración rectangular
    >>> integral_definida(1,2)
    6.747
    >>> integral_definida(0,2.5)
    17.246
    """
    N = 1000 # Número de rectángulos
    base = (b - a) / N # Base de los rectángulos
    suma = 0 # Se inicializa la suma
    for i in range(N): # Itera los rectángulos
        x = a + i * base # Lado x
        altura = 3 + x**3 # Calcula la altura
        suma += base * altura # Calcula el área
    return round(suma, 3) # Devuelve la suma total redondeada 3 decimales


# Comprobación de los resultados mostrándolos en pantalla
print(integral_definida(1,2))
print(integral_definida(0,2.5))


""" Ex 6 Suma de pares.   
   retorna la suma de los números pares n que no son múltiplos de b y 
   que  0 < n ≤ a.
  Por ejemplo suma_pares(10 , 3) es 2 + 4 + 8 + 10 = 24.
"""
def suma_pares(a, b):
    """
    Devuelve la suma de los números pares que no son múltiplos de b y que se encuentren entre este intervalo (0,a]
    >>> suma_pares(10, 3)
    24
    >>> suma_pares(12, 3)
    24
    >>> suma_pares(9, 1)
    0
    >>> suma_pares(16, 5)
    62
    >>> suma_pares(4, 4)
    2
    """
    suma = 0 # Inicializamos la suma
    for n in range (1, a+1): # Iteramos los numeros del 1 al a
        if n % 2 == 0 and n % b != 0: # Si n es par y no divisor de b
            suma += n # Sumamos n a la suma
    return suma # Devuelve la suma


# Comprobamos los resultados mostrándolos en pantalla
print(suma_pares(10, 3))
print(suma_pares(12, 3))
print(suma_pares(9, 1))
print(suma_pares(16, 5))
print(suma_pares(4, 4))


"""
 7. Suma de cuadrados impares
"""
def sumaCuadradosImpares(ini, fin):
    """
    Devuelve la suma de los cuadrados impares delimitados entre los parámetros de la función ambos incluidos, [ini, fin]
    >>> sumaCuadradosImpares(1,10)
    165
    >>> sumaCuadradosImpares(10,100)
    166485
    >>> sumaCuadradosImpares(10,101)
    176686
    """
    suma = 0 # Inicializamos la suma
    for i in range(ini, fin+1): # Iteramos desde el inicio (ini) hasta el final (fin)
        if i % 2 != 0: # Si el numero es impar
            suma += i ** 2 # Se añade el numero al cuadrado a la suma
    return suma # Devuelve la suma


# Comprobamos los resultados mostrandolos en pantalla
print(sumaCuadradosImpares(1, 10))
print(sumaCuadradosImpares(10, 100))
print(sumaCuadradosImpares(10, 101))


"""
8. Aproximación de pi
"""
# Dado num de terminos n
def pi_aprox(n):
    """
    Calcula la aproximación de pi usando la serie de Leibniz y devuelve pi redondeado a 12 decimales
    >>> pi_aprox(10)
    3.232315809406
    >>> pi_aprox(1000)
    3.14259165434
    >>> pi_aprox(10000000)
    3.14159275359
    """
    pi = 0 # Inicializamos la variable dónde almacenaremos el valor aprox de pi
    for i in range(n): # Bucle que recorre desde 0 hasta n-1
        pi += (-1)**i / (2 * i + 1) # Aplicamos la formula de la serie de Leibniz
    pi *= 4 # Multiplicamos el 4 que multiplica al sumatorio de la serie de Leibniz
    return round(pi, 12) # Devuelve pi redondeado a 12 decimales


# Comprobamos los resultados mostrándolos en pantalla
print(pi_aprox(10))
print(pi_aprox(1000))
print(pi_aprox(10000000))


# Aproximacion de pi hasta una precisión epsilon
def pi_aprox2(epsilon=1e-6):
    """
    Calcula la aproximación de pi usando la serie de Leibniz y un error épsilon dado.
    >>> pi_aprox2(1e-3)
    3.143588659586
    >>> pi_aprox2()
    3.141594653586
    >>> pi_aprox2(1e-7)
    3.14159285359
    """
    pi = 0 # Inicializamos la variable dónde se almacena el valor aprox de pi
    n = 0 # Inicializamos n
    signo = 1 # Definimos el signo positivo
    while (4/(2*n+1)) > epsilon: # Mientras el término sea mayor que épsilon:
        pi += signo * (4/(2*n+1)) # Sumamos el término a pi
        signo = -signo # Cambiamos el signo
        n = n + 1 # Incrementamos 1
    return pi # Se devuelve el valor de pi


# Comprobamos los resultados en pantalla
print(pi_aprox2(1e-3))
print(pi_aprox2())
print(pi_aprox2(1e-7))



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())