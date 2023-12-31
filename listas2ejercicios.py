# Seleccionar pieza del código y pulsar Ctrl + / 

## ---------------------- LISTAS II ------------------------
# texto = "Esto es una prueba"
# fecha = "16/10/2000"
# 1.1 EJERCICIOS
# print(len(texto),len(fecha))
# resultado = fecha + "-" + texto
# print(resultado)
# print("prueba" in str(texto).lower() or "esto" in str(texto).lower())
# print(texto.split())
# print(fecha.split("/"))
# vocales = "aeiou"
# for i in range(len(vocales)):
#     texto = str(texto).lower().replace(vocales[i],"i")
# print(texto)
# print(str(texto).lower().replace("is ","iri "))

## ---------------------- 1.2 EJERCICIOS ----------------------
# f = open("datos.txt")
# datos = f.readlines()
# print(datos)
# print(len(datos))
# print(datos[0])
# linea = datos[0].rstrip().split(" ")
# print(datos[0].split(" "))
# print(linea)
# f.close()

## ---------------------- 2.1 EJERCICIOS ----------------------

def fichero(strN):
    f = open(strN)
    datos = f.readlines()
    for i in range(len(datos)):
        datos[i] = int(datos[i].rstrip())
    return datos
# print(fichero("datos.txt"))
# suma = sum(fichero("datos.txt"))
# print(suma)

## ---------------------- 2.2 EJERCICIOS ----------------------
def ficheroStr(strN):
    f = open(strN)
    datos = f.readlines()
    for i in range(len(datos)):
        datos[i] = datos[i].rstrip()
    return datos
# print(len(ficheroStr("alumnos.txt")))

def coincide_apellido(index,strA):
    return strA.lower() in ficheroStr("alumnos.txt")[index].lower()
# print("".join(open("alumnos.txt").readlines()))
# s = int(input("Introduce el número de línea (empezando por cero) para leer el nombre: "))
# t = str(input("Introduce el apellido para checkear si lo tiene: "))
# print(coincide_apellido(s,t))
# allFernandez = 0
# for x in range(len(ficheroStr("alumnos.txt"))):
#     if(coincide_apellido(x,"Fernandez")):
#         allFernandez += 1
# porcentaje = (allFernandez/float(len(ficheroStr("alumnos.txt")))) * 100.0
# print(porcentaje)
def lenNombre(index):
    nombre = ficheroStr("alumnos.txt")[index].split(", ")[1]
    return len(nombre.split(" "))
# r = int(input("Introduce la línea para contar las palabras del nombre: "))
# print(lenNombre(r))
# cantidadNombres = [0,0,0,0,0,0,0,0] # te ahorro tiempo, 8 ceros
# for j in range(len(ficheroStr("alumnos.txt"))):
#     cantidadNombres[lenNombre(j)] = cantidadNombres[lenNombre(j)]+1
#     if(sum(cantidadNombres) >= len(ficheroStr("alumnos.txt"))):
#         break
#
# print(cantidadNombres)

## ---------------------- EJERCICIOS 3 (OPCIONAL) ----------------------

## Exportar a ".CSV (Delimitado por comas)"
## Eliminar antes la primera línea con el editor de texto
listaCompleta = ficheroStr("datos-paises.csv")
print(ficheroStr("datos-paises.csv"))
listaPaises = []
listaPoblacion = []
listaTelefs = []
for k in range(1,len(listaCompleta),1):
    listaPaises.append(str(listaCompleta[k].split(";")[0]))
for l in range(1,len(listaCompleta),1):
    listaPoblacion.append(int(listaCompleta[l].split(";")[1]))
for m in range(1,len(listaCompleta),1):
    listaTelefs.append(int(listaCompleta[m].split(";")[2]))
poblacionTotal = sum(listaPoblacion)
print("Población total:",poblacionTotal)
promedioHabPorPais = poblacionTotal/len(listaPaises)
print("Habitantes por pais promedio:",promedioHabPorPais)
listaPromedioTelefs = []
for a in range(len(listaCompleta)-1):
    listaPromedioTelefs.append(float(listaTelefs[a]/listaPoblacion[a]))
print(listaPromedioTelefs)
