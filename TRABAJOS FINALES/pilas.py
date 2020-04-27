"""
PROGRAMA CON EL OBJETIVO DE AYUDAR A UNA BIBLIOTECA
Andrea Sarai Juárez Munguia
TI 41
"""
#CREACION DE LAS LISTAS/PILAS
pila1=['Enciclopedia Encarta','Blancanieves','Investigación & Desarrollo','Revista de Derecho']
pila2=['Enciclopedia Labor','Peter Pan','Enciclopedia Libre Universal','Pensamiento y Gestión']
enciclopedia=[]
cuentos=[]
otros=[]

#CREACION DEL MENU
print("----------------------------------- B I E N V E N I D O S -----------------------------------")
print("------------------------------- M E N U  D E  O P C I O N E S -------------------------------")
print("1.- INGRESAR ELEMENTO")
print("2.- ELIMINAR ELEMENTO")
print("3.- MOSTAR PILA")
print("4.- MOSTRAR TAMAÑO DE LA PILA")
print("5.- SALIR")
opcion=int(input("INGRESE LA OPCION QUE DESEA ELEGIR: "))

#OPCION 1 DE INGRESAR
if opcion == 1:
    print(" ENCICLOPEDIA \n CUENTOS \n OTROS")
    print("---- F A V O R  D E  I N G R E S A R  L A  O P C I O N  E N  M A Y U S C U L A S ----")
    ingresar1=input("¿A QUE PILA DESEA INGRESAR UN NUEVO ELEMENTO? ")
    if ingresar1 == "ENCICLOPEDIA":
        elemento=input("INGRESE EL NOMBRE DEL ELEMENTO A APILAR: ")
        enciclopedia.append(elemento)
        print("")
        print("E L E M E N T O  I N G R E S A D O")
        print(enciclopedia)

    elif ingresar1 == "CUENTOS":
        elemento=str(input("INGRESE EL NOMBRE DEL ELEMENTO A APILAR: "))
        cuentos.append(elemento)
        print("")
        print("E L E M E N T O  I N G R E S A D O")

    elif ingresar1 == "OTROS":
        elemento=str(input("INGRESE EL NOMBRE DEL ELEMENTO A APILAR: "))
        otros.append(elemento)
        print("")
        print("E L E M E N T O  I N G R E S A D O")

    else:
        print("INTENTELO DE NUEVO")

#OPCION 2 DE ELIMINAR
elif opcion == 2:
    print(" ENCICLOPEDIA \n CUENTOS \n OTROS \n PILA 1 \n PILA 2")
    print("---- F A V O R  D E  I N G R E S A R  L A  O P C I O N  E N  M A Y U S C U L A S ----")
    ingresar2=input("¿A QUE PILA DESEA ELIMINAR UN NUEVO ELEMENTO? ")
    if ingresar2 == "ENCICLOPEDIA":
        if len(enciclopedia) == 0:
            print("NO  HAY ELEMENTOS PARA ELIMINAR")
        else:
            enciclopedia.pop()
            print("EL ELEMENTO FUE ELIMINADO")
        
    #elif ingresar2 == "CUENTOS":

    #elif ingresar2 == "OTROS":

    elif ingresar2 == "PILA 1":
        if len(pila1) == 0:
            print("NO  HAY ELEMENTOS PARA ELIMINAR")
        else:
            pila1.pop()
            print("EL ELEMENTO FUE ELIMINADO")

    elif ingresar2 == "PILA 2":
        if len(pila2) == 0:
            print("NO  HAY ELEMENTOS PARA ELIMINAR")
        else:
            pila2.pop()
            print("EL ELEMENTO FUE ELIMINADO")

    else:
         print("INTENTELO DE NUEVO")