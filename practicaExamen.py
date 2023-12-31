from functools import reduce

from unicodedata import decimal


# EJERCICIO 7 Y 8
# [a,b] = [int(input("Introduce el número inicial de \"a\",  mayor que cero: ")),int(input("Introduce el límite (b) mayor que \"a\": "))]
# resultado = 1
# for i in range(a,b,1):
#     resultado += ((i**2) + 1)/i
# print(resultado)


# EJERCICIO 9
def esPar(n):
    return n & 1 != 1
# [a,b] = [int(input("Introduce el inicio del intervalo: ")),int(input("Introduce el final del intervalo: "))]
# for i in range(a,b,1):
#     print(i,"es par" if esPar(i) else "es impar")

# EJERCICIO 11 PORQUE EL 10 ME CAE MAL
# n = int(input("Introduce el número parar conseguir los divisores"))
# divisoresResultado = ""
# for i in range(1,n+1,1):
#     if(n%i == 0):
#         divisoresResultado += f" {i}"
# print(divisoresResultado)

# EJERCICIO 13 PORQUE EL 12 LO HICE EN CLASE
# n = int(input("Introduce un número para generar los números de Perrin: ")); perrinStr = ""
def Perrin(m):
    if(m == 0):
        return 3
    elif(m == 1):
        return 0
    elif(m == 2):
        return 2
    else: return Perrin(m-2) + Perrin(m-3)
#
# for i in range(0,n,1):
#     perrinStr += f"{Perrin(i)}, "
# print(perrinStr)
#_________________________________________________________________________

# EJERCICIO 1 FUNCIONES
def factorial(num):
    if(num == 0):
        return 1
    elif(num < 0):
        return None
    else:
        return reduce(lambda a, b: a*b, range(1,num+1))
# n = int(input("Introduce un número positivo (mayor que 0), para obtener su factorial: "))
# print(f"El número es: {n}\nSu factorial es: {factorial(n)}")

# EJERCICIO 2
def getSumaLista(arr):
    resultado = 0
    for x in range(len(arr)):
        resultado += arr[x]
    return resultado

def getDivisores(num):
    divisores = []
    for i in range(1,num,1):
        if(num%i == 0):
            divisores.append(i)
    return divisores

def esPerfecto(num):
    return getSumaLista(getDivisores(num)) == num

def esPerfectoBinario(n):
    nStr = str(bin(n))
    nStr = n[2:len(n)]
    if((n != 6) and esPar(nStr.count("0")) == False):
        return False
    return (int(nStr.count("1")) -1) == nStr.count("0")

def binario_a_decimal(numero_binario):
	numero_decimal = 0
	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion
	return numero_decimal
# s = int(input("Introduce el número para comprobar si es perfecto: "))
# print("El número","es perfecto" if esPerfecto(s) else "no es perfecto")

# EJERCICIO 9 Y 10 PORQUE NO ME QUEDA MUCHO TIEMPO
def Fibonacci(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
# t = int(input("Introduce el número (indice) de la sucesion Fibonacci para obtenerlo: "))
# print(t,"->",Fibonacci(t))







