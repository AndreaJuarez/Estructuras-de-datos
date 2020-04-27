# encoding: utf-8
print("PRACTICA NUMERO 2: INVERSION DE DATOS")

array=[]
dimension=int(input("INGRESE EL NUMERO DE ELEMENTOS DE ARREGLO: "))

#INGRESO DE ELEMENTOS
while True:
    if dimension !=0:
            num=int(input("Ingrese el nuevo valor: "))
            array.append(num)
            dimension=dimension-1
    else:
        break

arrayinvertido=[]
arrayinvertido=array[::-1] #Los dos puntos significan inicio y fin, y el -1 significa en que orden segun iran

print("")
print("EL PRIMER ARREGLO ES:")
print(array)
print("")
print("EL ARREGLO INVERTIDO ES:")
print(arrayinvertido)



