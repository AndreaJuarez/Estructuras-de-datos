print("PRACTICA 6: MULTIPLICACION DE MATRICES")
print("------------------------------------------------------------------------")

#---------------------------------------MATRIZ UNO----------------------------------------------------
#INSERCION DE NUMERO DE FILA Y COLUMNA DE LAS MATRICES
fila1=int(input("INTRODUCE EL NUMERO DE FILAS: "))
columna1=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))
array1=[]
#VALIDACION DE MATRIZ CUADRADA
while True:
    if fila1 != columna1 or columna1 != fila1:
      print("LA MATRIZ DEBE SER CUADRADA, INGRESE LOS VALORES DE NUEVO")
      print("-------------------------------------------------------------------")
      print("-------------------------CREACION MATRIZ UNO-----------------------")
      fila1=int(input("INTRODUCE EL NUMERO DE FILAS: "))
      columna1=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))
    else:
        break
#FORMATO DE LA MATRIZ UNO
for x in range(fila1):
     array1.append([0]*columna1)
#INSERCION DE DATOS DE LA MATRIZ UNO
print("--------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ UNO ---------")
for f1 in range(fila1): 
    for c1 in range(columna1):
        array1[f1][c1]=float(input("ELEMENTO A INGRESAR:"))


#---------------------------------------MATRIZ DOS-----------------------------------------------------
#INSERCION DE NUMERO DE FILA Y COLUMNA DE MATRIZ DOS
print("-------------------------CREACION MATRIZ DOS-----------------------")
fila2=fila1
columna2=columna1
array2=[]
#FORMATO DE LA MATRIZ DOS
for y in range(fila2):
     array2.append([0]*columna2)
#INSERCION DE DATOS DE LA MATRIZ DOS
print("------------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ DOS ------------")
for f2 in range(fila2): 
    for c2 in range(columna2):
        array2[f2][c2]=float(input("ELEMENTO A INGRESAR:"))

#IMPRESION MATRIZ UNO
print("LA MATRIZ UNO ES: ")
for a in array1:
    print(a)

#IMPRESION MATRIZ DOS
print("LA MATRIZ DOS ES: ")
for b in array2:
    print(b)


#-----------------------------------------FUNCIONALIDAD---------------------------------------------
array3=[]             #Declaracion del tercer array

#DAR FORMATO A LA MATRIZ
for x in range(fila1):
     array3.append([0]*fila2)


for f1 in range(fila1):
    for c1 in range(fila2):
        for c2 in range(fila2):
            #ERROR QUE TENIA EN ESTA LINEA: can't multiply sequence by non-int of type 'str'
            array3[f1][c2]+=array1[f1][c1]*array2[c1][c2]
print("LA MATRIZ TRES ES: ")
for e in array3:
    print(e)

#El error se resolvio, añadiendo float al momento de pedir el dato de entrada para el valor de la matriz0