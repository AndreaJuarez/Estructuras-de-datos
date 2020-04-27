# encoding: utf-8
print("PRACTICA NUMERO 1: INSERCION Y BUSQUEDA")

array=[]
dimension=int(input("Ingrese el numero de elementos del arreglo: "))

#INGRESO DE ELEMENTOS
while True: #Siempre va a ser evaluada como verdadera por definición, hasta romper el ciclo con break
    if dimension !=0:
            num=int(input("Ingrese el nuevo valor: "))
            array.append(num) #append, agrega su argumento como un elemento único al final de una lista
            dimension=dimension-1
    else:
        break
print(array)

#BUSQUEDA DE ELEMENTOS
inicio=0
longitud= len(array) #len, devuelve el número de elementos en un objeto
encontrado=False
buscado=int(input("Ingrese el elemento que desee buscar: "))

#BUSQUEDA BINARIA
while not encontrado and inicio <= longitud:
    mitad = int((inicio+longitud) / 2) #Se saca la mitad del arreglo unidimensional
    if buscado == array[mitad]: #Se evalua si ese es el numero que se esta buscando
        encontrado=True         #Se vuelve verdadero porque ya se encontro
    elif buscado < array[mitad]: #elif,se utiliza para enlazar varios else if,sería «si es»
        longitud = mitad - 1     #Si buscado es menor al numero que se encuentra a la mitad, se restara uno
    else:                       #Si no, se sumara uno para asi ir buscando
        inicio = mitad + 1

if encontrado:
    print("El dato se encuentra en la posicion ", str(mitad+1))
    print(array)
else:
            print("El dato no se encontro")
