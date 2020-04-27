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

#----------------------------MANERA EN QUE LA MISS EXPLICO COMO SE HACE------------------------------
array2=[]                             #Declaracion del otro array para imprimir el array unidimensional resultante
for f in range(fila):                 #Mediante un ciclo for, se repetira hasta el numero de filas
    for c in range(columna):          #Mediante un ciclo for, se repetira hasta el numero de columnas
        if c ==f:                 #Condicion para evaluar si la fila y columna es igual, se ira agregando el valor al otro vector
         array2.append(array[f][c])        #Se agregara en el array 2, lo que encuentre en el array uno y que esta evaluando en los for
print("LA DIAGONAL ES:")
print(array2)

#Como para sacar la diagonal se imprimiran los valores que esten en posiciones iguales,
# por eso se evalua con el if