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
array11=[]
array22=[]

#DECLARACION DE TAMAÑO DE ARRAY TRES
if fila1 > fila2:
    fila3 = fila1
    if columna1 > columna2:
        columna3 = columna1
    else:
        columna3 = columna2
else:
    fila3 = fila2
    if columna1 > columna2:
        columna3 = columna1
    else:
        columna3 = columna2

for i in range(fila3):
    array3.append([0]*columna3)
    array11.append([0]*columna3)
    array22.append([0]*columna3)

for i in range(fila1):
    for j in range(columna1):
        array11[i][j]=array1[i][j]
for i in range(fila2):
    for j in range(columna2):
        array22[i][j]=array2[i][j]

for i in range(fila3):
    for j in range(columna3):
        array3[i][j]=(array11[i][j])+(array22[i][j])

print("LA MATRIZ RESULTANTE ES:")
for u in array3:
    print(u)