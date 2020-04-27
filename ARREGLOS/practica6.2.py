print("PRACTICA 6: MULTIPLICACION DE MATRICES")
print("------------------------------------------------------------------------")

#---------------------------------------MATRIZ UNO----------------------------------------------------
#INSERCION DE NUMERO DE FILA Y COLUMNA DE LAS MATRICES
array1=[]
tamaño=int(input("INTRODUCE EL TAMAÑO DE LA MATRIZ: "))
#FORMATO DE LA MATRIZ UNO
for x in range(tamaño):
     array1.append([0]*tamaño)

#INSERCION DE DATOS DE LA MATRIZ UNO
print("--------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ UNO ---------")
for f in range(tamaño): 
    for c in range(tamaño):
        array1[f][c]=input("ELEMENTO A INGRESAR EN LA POSICION" + " "+ str(f) + (",") + str(c) + ": ")  


#---------------------------------------MATRIZ DOS-----------------------------------------------------
#INSERCION DE NUMERO DE FILA Y COLUMNA DE MATRIZ DOS
print("-------------------------CREACION MATRIZ DOS-----------------------")
array2=[]
tamaño2=tamaño

#FORMATO DE LA MATRIZ DOS
for y in range(tamaño2):
     array2.append([0]*tamaño2)

#INSERCION DE DATOS DE LA MATRIZ DOS
print("------------- INTRODUCE LOS ELEMENTOS DE LA MATRIZ DOS ------------")
for f2 in range(tamaño2): 
    for c2 in range(tamaño2):
        array2[f2][c2]=input("ELEMENTO A INGRESAR EN LA POSICION " + str(f2) + (",") + str(c2) + (": "))

#IMPRESION MATRIZ UNO
print("LA MATRIZ UNO ES: ")
for a in array1:
    print(a)

#IMPRESION MATRIZ DOS
print("LA MATRIZ DOS ES: ")
for b in array2:
    print(b)


#-----------------------------------------FUNCIONALIDAD---------------------------------------------
array3=[]

for x in range(tamaño):
   array3.append([0]*tamaño2)

for f in range(tamaño):
    for c2 in range(tamaño2):
     for c in range(tamaño2):
        array3[f][c2]+=array1[f][c]*array2[c][c2]

print("LA MATRIZ TRES ES: ")
for e in array3:
    print(e)
