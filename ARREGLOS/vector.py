arreglo=[]
tamaño = int(input("Ingresa el tamaño de la matriz: "))
for r in range(tamaño):
  arreglo.append([0]*tamaño) #crea los espacios del arreglo.
for i in range(tamaño):
  for j in range(tamaño):
    arreglo[i][j]= int(input("Numero: "+"Posicion "+str(i)+" , "+str(j)+" "+": "))
for e in (arreglo):
  print(e)
arreglo2=[0 for x in range(tamaño)] #para definir el tamaño del areglo igual al de la matriz 
d=0 #contador para la posicion de arreglo
i=0
j=0
while d != tamaño:
    arreglo2[d]=arreglo[i][j]
    d=d+1
    i=i+1
    j=j+1
print("Este es el vetor de la matriz:",arreglo2)