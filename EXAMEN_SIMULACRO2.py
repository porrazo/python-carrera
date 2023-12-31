from functools import reduce
from sympy import *
from numpy import matmul


# EJERCICIO 1
# s = str(input("Introduzca un carácter (\".\" para terminar): "))
# while("." not in s):
#     s += str(input("Introduzca un carácter (\".\" para terminar): "))
# print(f"Se repite {s.count('a')} veces.")

# EJERCICIO 2
# n = int(input("Introduzca un número entero: "))
# while(n < 0):
#     print(n)
#     n = int(input("Introduzca un número entero: "))

# EJERCICIO 12
# n = int(input("Introduce un número natural: "))
def esPrimo(num):
    for N in range(2,int(num**0.5)+1):
        if num%N == 0:
            return False
    if(num==1):
        return False
    return True
def esPrimoConsola(n):
    print("El número es primo" if all(n%i for i in range(2,n)) else "El número no es primo")
# print(esPrimoConsola(n))

# FUNCIONES 2!!!!!!!!!!!!!!!!!!!!!!

# EJERCICIO 1
def lee_entero():
    return int(input("Introduzca un número entero: "))
def mayor2(n,m):
    return max(n,m)
# [a,b] = [lee_entero(),lee_entero()]
# print(mayor2(a,b))

# EJERCICIO 2
def mayor3(x,y,z):
    return mayor2(mayor2(x,y),z)
# [a,b,c] = [lee_entero(),lee_entero(),lee_entero()]
# print(mayor3(a,b,c))

# EJERCICIO 5
# nota = float(input("Introduce la nota del alumno: "))
# def calificacion(f):
#     resultado = ""
#     if(f < 5):
#         resultado = "suspenso"
#     elif(5 <= f < 7):
#         resultado = "aprobado"
#     elif(7 <= f < 9):
#         resultado = "notable"
#     elif(9 <= f < 10):
#         resultado = "sobresaliente"
#     elif(f == 10):
#         resultado = "matrícula de honor"
#     return resultado + ", " + str(f)
#
# print(calificacion(nota))

# FUNCIONES 2 (PENSABA QUE ESTABA HACIENDOLO YA), EJERCICIO 1

# num = int(input("Introduzca un número para ver su factorial: "))
def factorial(n):
    return reduce(lambda a,b: a*b, range(1,n+1))
# print(str(num) + ", " + str(factorial(num)))

# EJERCICIO 2

def getDivisoresSuma(n):
    lista = []
    for i in range(1,n-1):
        if(n%i==0):
            lista.append(i)
    return sum(lista)
def esPerfecto(n):
    return n==getDivisoresSuma(n)

# EJERCICIO 4

# num = int(input("Introduzca si el número es primo: "))

def esPrimoBooleano(n):
    return (n != 1 if all(n%i for i in range(2,n)) else False)

# while(num >= 0):
#     print(f"El número {num} {'en efecto' if esPrimoBooleano(num) else 'no'} es primo")
#     num = int(input("Introduzca si el número es primo: "))

# EJERCICIO 7

def linea(ch, n):
    return str(ch*n)

def cuadrado(ch,n):
    cadena = ""
    for i in range(n):
        cadena += linea(ch, n*2) + "\n"
    return cadena
# print(cuadrado('*',3))

# EXTRA (BASE 17)

# 9 -> "9"
# 10 -> "A"
# 17 -> "10" // X en base Y = Y en base X
# 20 -> "13"
# 33 -> "1G"
