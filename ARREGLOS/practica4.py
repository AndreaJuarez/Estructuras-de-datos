print("PRACTICA 4: OBTENCIÓN DE DIAGONAL DE UNA MATRIZ CUADRADA")
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

#OBTENCION DE DIAGONAL DE LA MATRIZ

#----------------------------CHECAR ESTA MANERA DE RESOLVER------------------------------
#array2=[]                             #Declaracion del otro array para imprimir el array unidimensional resultante
#for f in range(fila):                 #Mediante un ciclo for, se repetira hasta el numero de filas
 #    array2.append(array[f][f])        #Se agregara en el array 2, 
#print(array2)

#----------------------------MANERA EN QUE FER ME ENSEÑO-------------------------------
arreglo2=[0 for x in range(fila)] #para definir el tamaño del areglo igual al de la matriz
contador=0 #variable que ira contando para la posicion de arreglo(diagonal)
f=0        #variable de filas, se inicializa en 0, para que vaya incrementando
c=0        #variable de columnas, se inicializa en 0 para que vaya incrementando

while contador != fila:         #condicion, mientras el contador sea diferente a el numero de filas o columnas, no importa el dato porque es una matriz cuadrada
    arreglo2[contador]=array[f][c]      #arreglo2, en la variable contador será las variables de fila y columna
    contador=contador+1
    f=f+1
    c=c+1
print("LA DIAGONAL DE LA MATRIZ SERA:",arreglo2)