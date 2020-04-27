print("EXAMEN UNIDAD 2: SUMA DE MATRICES DE CUALQUIER DIMENSION")
print("17/02/2020")
print("--------------------------------------------------------")

#---------------------------------------MATRIZ UNO----------------------------------------------------
#INSERCION DE NUMERO DE FILA Y COLUMNA DE LAS MATRICES
array1=[]
print("--------------------MATRIZ UNO--------------------------")
fila1=int(input("INTRODUCE EL NUMERO DE FILAS: "))
columna1=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))

#FORMATO E INSERCION DE DATOS DE LA MATRIZ UNO
for x in range(fila1):
     array1.append([0]*columna1)

print("--------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ UNO ---------")
for f1 in range(0,fila1): 
    for c1 in range(0,columna1):
        array1[f1][c1]=float(input("ELEMENTO A INGRESAR EN LA POSICION " + str(f1) + (",") + str(c1) + ": "))

#---------------------------------------MATRIZ DOS----------------------------------------------------
#INSERCION DE NUMERO DE FILA Y COLUMNA DE LAS MATRICES
array2=[]
print("-------------------MATRIZ DOS---------------------------")
fila2=int(input("INTRODUCE EL NUMERO DE FILAS: "))
columna2=int(input("INTRODUCE EL NUMERO DE COLUMNAS: "))

#FORMATO E INSERCION DE DATOS DE LA MATRIZ DOS
for y in range(fila2):
    array2.append([0]*columna2)

print("---------INTRODUEC LOS ELEMENTOS DE LA MATRIZ DOS-----------")
for f2 in range(0,fila2):
    for c2 in range(0,columna2):
        array2[f2][c2]=float(input("ELEMENTOS A INGRESAR EN LA POSICION " + str(f2) + (",") + str(c2) + ":"))

#------------------------------------------IMPRESION DE MATRICES-----------------------------------------
print("LA MATRIZ UNO ES:")
for a in array1:
    print(a)

print("LA MATRIZ DOS ES:")
for b in array2:
    print(b)

#-----------------------------------------FUNCIONALIDAD---------------------------------------------
array3=[]

for x in range(fila1):
    array3.append([0]*columna1)

#SUMA
for c in range(columna1):
    for f in range(fila1):
            array3[f][c]=array2[f][c]++array1[f][c]

print("EL RESULTADO EN MATRIZ ES: ")
for e in array3:
    print(e)
