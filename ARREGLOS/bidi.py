# encoding: utf-8
print("PRACTICA 3: INSERCION Y BUSQUEDA EN ARREGLOS BIDIMENSIONALES")

fila=int(input("INGRESE EL NUMERO DE FILAS: "))
columna=int(input("INGRESE EL NUMERO DE COLUMNAS: "))
array=[]

#INGRESO DE ELEMENTOS
while True:
    if fila !=0:
        if columna !=0:
            numcolumna=int(input("Ingrese el nuevo valor: "))
            array.append(numcolumna)
            columna=columna-1
            numfila=int(input("Ingrese el nuevo valor: "))
            array.append(numfila)
            fila=fila-1
    else:
        break
print(array)

