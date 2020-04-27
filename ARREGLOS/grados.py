lista=[]
num=int(input("Ingrese el numero de temperaturas a capturar: "))

while True:
    if num !=0:
            temperatura=int(input("Ingrese el valor de la temperatura: "))
            lista.append(temperatura)
            num=num-1
    else:
        break
#print(lista)
promedio = sum(lista)/float(len(lista))
print("El promedio en celcius es:", promedio)

fahrenheit = (promedio * 1.8) + 32
print("El promedio en farenheit es:", fahrenheit)