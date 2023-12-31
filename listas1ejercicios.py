# LISTAS I
# EJERCICIOS 1.1
lista1 = [5,8,10]
lista2 = [3,2,9,12,4]
# print(len(lista1),len(lista2))
# print(len(lista1 + lista2))
# print(max(max(lista1),max(lista2)))
# print(max(lista1 + lista2))
# EJERCICIOS 1.2
# print(lista1[0] + lista2[0])
# print(lista1[len(lista1)-1] + lista2[len(lista2)-1])
# while(8 in lista1):
#     lista1[lista1.index(8)] = 0
# print(lista1)

# EJERCICIOS 1.3
# lista3 = lista2
# print(lista3)
# lista3[0] = 7
# print(lista3)
# print(lista2)

# EJERCICIOS 1.4
# for i in range(len(lista1)):
#     print(lista1[i])
# print("\n")
# for j in range(len(lista2)-1,-1,-1):
#     print(lista2[j])
# count = 0;
# for k in range(len(lista2)):
#     count += lista2[k]
# print(count,sum(lista2))

# EJERCICIOS 2.1
def sumatorio(lista):
    count = 0
    for i in range(len(lista)):
        count += lista[i]
    return count
ejemplo = [5,5,5,5,5,5] # 5*6 = 30
# print(sumatorio(ejemplo),sum(ejemplo))

# EJERCICIOS 2.2
def mayorElemento(lista):
    return lista.index(max(lista))
datos = [4,2,7,1,3]
# print(mayorElemento(datos))

# EJERCICIOS 2.3
def quitarNegativos(lista):
    count = 0
    for i in range(len(lista)):
        if(lista[i] < 0):
            count +=1
            lista[i] = 0
    return count
datos2 = [3, -4, 5, 7, -1, 8]
print(quitarNegativos(datos2))
# print(datos2)

# EJERCICIO FINAL OPCIONAL
def sumaPotencia(lista,pow):
    for i in range(len(lista)):
        lista[i] **= pow
    return sumatorio(lista)
print(str(sumaPotencia(datos,2)) + "\n" + str(sumaPotencia(datos2,0.5)) + "\n" + str(sumaPotencia(lista1,0)))
