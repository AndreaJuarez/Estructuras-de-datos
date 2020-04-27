print("PRACTICA 5: INTERCAMBIO DE FILAS Y COLUMNAS EN MATRIZ CUADRADA")
print("---------------------------------------------------------")

#INSERCION DE NUMERO DE FILA Y COLUMNA
fila=int(input("INTRODUCE EL NUMERO DE FILAS: "))
columna=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))
array=[]

#VALIDACION DE MATRIZ CUADRADA
while True:
    if fila != columna or columna != fila:
      print("LA MATRIZ DEBE SER CUADRADA, INGRESE LOS VALORES DE NUEVO")
      print("---------------------------------------------------------")
      fila=int(input("INTRODUCE EL NUMERO DE FILAS: "))
      columna=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))
    else:
        break

#FORMATO DE LA MATRIZ
for m in range(fila):
     array.append([0]*columna)
print("EL FORMATO SERÁ:")
for a in array:
    print(a)

#INSERCION DE DATOS
print("--------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ ---------")
for f in range(0,fila): 
    for c in range(0,columna):
        array[f][c]=input("ELEMENTO A INGRESAR EN LA POSICION " + str(f) + (",") + str(c) + ": ")  
for a in array:
    print(a)

#INTERCAMBIO DE FILAS Y COLUMNAS
print("--------------------------------------------------------")

#------------------------------DE ESTA FORMA LO IMPRIME COMO LISTA-----------------------------------
#array2=[]
#for f in range(0,fila):
 #   for c in range(0,columna):
  #      nc=f
   #     nf=c
    #    array2[f][c].append(array2[nc][nf])
#print(array2)

#-------------------------------DE ESTA FORMA SI SALE-------------------------------------------
array2=[]
#Para darle formato
for k in range(fila):           #for para tamaño de la matriz
    array2.append([0]*fila)     #lo ira llenando con ceros

for f in range(0,fila):         #comenzara a recorrer la matriz, desde cero hasta fila
    for c in range(0,columna):
       nc=f
       nf=c
       array2[c][f]=array[nc][nf]
print("LA NUEVA MATRIZ SERA:")
for a in array2:
    print(a)