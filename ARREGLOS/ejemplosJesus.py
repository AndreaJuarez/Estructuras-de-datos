S=0
array=[[]]
while True:
    while True:
        colocar=input("Colocar valor y poner f para terminar")
        if colocar == "f":
            break
        else:
            array[S].append([(int(colocar))])
    cambio = input("Desea agregar otra lista? s/n")
    if cambio == "s":
        array.append([])
        s=s+1
    elif cambio == "n":
        break

