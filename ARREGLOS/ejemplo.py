# encoding: utf-8
print("PRACTICA 3: INSERCION Y BUSQUEDA EN ARREGLO BIDIMENSIONAL")
print("---------------------------------------------------------")

#INSERCION DE NUMERO DE FILA Y COLUMNA
fila=int(input("INTRODUCE EL NUMERO DE FILAS: "))
columna=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))
array=[]
for i in range(fila):
     array.append([0]*columna)
#print(array)

#INSERCION DE ELEMENTOS
print("--------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ ---------")
for f in range(0,fila): 
    for c in range(0,columna):
        array[f][c]=input("ELEMENTO A INGRESAR EN LA POSICION " + str(f) + (",") + str(c) + ": ")  
print(array)

#BUSQUEDA DE ELEMENTOS
print("------------ BUSCAR DE ELEMENTO POR POSICION -----------")
busquedafila=int(input("INGRESE EL NUMERO DE FILA: "))
busquedacolumna=int(input("INGRESE EL NUMERO DE COLUMNA: "))

if busquedafila <= fila:
    if busquedacolumna <= columna: 
        print("EL ELEMENTO SE ENCUENTRA EN: " )






