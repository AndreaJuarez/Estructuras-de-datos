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

#DECLARACION DE TAMAÑO DE ARRAY TRES
if fila1>fila2:
    fila3=fila1
else:
    fila3=fila2

if columna1>columna2:
    columna3=columna1
else:
    columna3=columna2

for z in range(fila3):
     array3.append([0]*columna3)

#SUMA
try:
    for c in range(columna1):
        for f in range(fila1):
                array3[f][c]=array1[f][c]++array2[f][c]
except:
    for c in range(columna1):
        for f in range(fila1):
            if array3[f][c]==0:
                array3[f][c]=array1[f][c] or array2[f][c]

try:
    for f in range(fila1):
        for c in range(columna1):
                array3[f][c]=array1[f][c]++array2[f][c]
except:
    for f in range(fila1):
        for c in range(columna1):
            if array3[f][c]==0:
                array3[f][c]=array1[f][c] or array2[f][c]

print("EL RESULTADO EN MATRIZ ES: ")
for e in array3:
    print(e)

#NOTA:SOLO DA TODOS LOS VALORES CORRECTAMENTE SI LAS DIMENSIONES SON IGUALES O SI
#EL NUMERO DE FILAS ES IGUAL O LA MATRIZ UNO ES MAYOR

#-----------------------------------------------------------------------------------------
#Lo que falto fue pasar a otro array mi array1 y array2 para que quedaran del mismo tamaño
#del array3 y asi fuera mas facil la suma, en ese caso ya no se tendria que hacer el try except
#para el llenado de los valores que queden en cero