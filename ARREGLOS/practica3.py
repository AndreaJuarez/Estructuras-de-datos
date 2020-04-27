# encoding: utf-8
print("PRACTICA 3: INSERCION Y BUSQUEDA EN ARREGLO BIDIMENSIONAL")
print("---------------------------------------------------------")

#INSERCION DE NUMERO DE FILA Y COLUMNA
fila=int(input("INTRODUCE EL NUMERO DE FILAS: "))
columna=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))
array=[]
#INICIALIZACIÓN DE LA MATRIZ
for i in range(fila):  #Iniciara la matriz, creando la estructura
     array.append([0]*columna)  #Llenando de ceros las filas y columnas 
print("EL FORMATO SERÁ:")
for b in array:          #Forma de imprimir en forma de matriz mediante un ciclo for
    print(b)

#INSERCION DE ELEMENTOS
print("--------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ ---------")
for f in range(0,fila):      #Ciclo for, indica el numero de repeticiones
    for c in range(0,columna):    #Range, es el rango. En este caso de 0 hasta el valor de fila y columna
        array[f][c]=input("ELEMENTO A INGRESAR EN LA POSICION " + str(f) + (",") + str(c) + ": ")  #str, forma de sustituir valores en las cadenas, metodo de salida(concatena)
for a in array:      #Impresion en forma de matriz
    print(a)

#BUSQUEDA DE ELEMENTOS
print("------------ BUSCAR DE ELEMENTO POR POSICION -----------")
busquedaf=int(input("INGRESE EL NUMERO DE FILA: "))
busquedac=int(input("INGRESE EL NUMERO DE COLUMNA: "))

if busquedaf < fila:               #If anidado,evalua si fila y columna son menores al numero existente de filas y columnas
    if busquedac < columna:        #Si es cierto, imprimira el numero de las posiciones que se estan ingresando
        print("EL ELEMENTO ES: ")
        print(array[busquedaf][busquedac])
    else:
        print("ELEMENTO NO EXISTENTE EN LA MATRIZ")
else:
    print("ELEMENTO NO EXISTENTE EN LA MATRIZ")