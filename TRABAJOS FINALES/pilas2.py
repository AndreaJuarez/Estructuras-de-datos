"""
PROGRAMA CON EL OBJETIVO DE AYUDAR A UNA BIBLIOTECA
Andrea Sarai Juárez Munguia
TI 41
"""
#CREACION DE LAS PILAS
pila1=['Enciclopedia Encarta','Blancanieves','Investigación & Desarrollo','Revista de Derecho']
pila2=['Enciclopedia Labor','Peter Pan','Enciclopedia Libre Universal','Pensamiento y Gestión']
enciclopedia=[]
cuentos=[]
otros=[]

#CREACION DEL MENU
def main():
    print("----------------------------------- B I E N V E N I D O S -----------------------------------")
    print("------------------------------- M E N U  D E  O P C I O N E S -------------------------------")
    print("1.- INGRESAR ELEMENTO")
    print("2.- ELIMINAR ELEMENTO")
    print("3.- MOSTAR PILA")
    print("4.- LIBROS EXISTENTES EN LA PILA")
    print("5.- SALIR")
    opcion=int(input("INGRESE LA OPCION QUE DESEA ELEGIR: "))

    #OPCION 1 DE INGRESAR
    if opcion == 1:
        print("PILAS A LAS QUE LE PUEDE INGRESAR:")
        print(" ENCICLOPEDIA \n CUENTOS \n OTROS")
        print("---- F A V O R  D E  I N G R E S A R  L A  O P C I O N  E N  M A Y U S C U L A S ----")
        ingresar1=input("¿A QUE PILA DESEA INGRESAR UN NUEVO ELEMENTO? ")
        if ingresar1 == "ENCICLOPEDIA":
            elemento=input("INGRESE EL NOMBRE DEL ELEMENTO A APILAR: ")
            enciclopedia.append(elemento)
            print("")
            print("E L E M E N T O  I N G R E S A D O")
            print(enciclopedia)
            main()

        elif ingresar1 == "CUENTOS":
            elemento=str(input("INGRESE EL NOMBRE DEL ELEMENTO A APILAR: "))
            cuentos.append(elemento)
            print("")
            print("E L E M E N T O  I N G R E S A D O")
            print(cuentos)
            main()

        elif ingresar1 == "OTROS":
            elemento=str(input("INGRESE EL NOMBRE DEL ELEMENTO A APILAR: "))
            otros.append(elemento)
            print("")
            print("E L E M E N T O  I N G R E S A D O")
            print(otros)
            main()

        else:
            print("INTENTELO DE NUEVO")
            main()

    #OPCION 2 DE ELIMINAR
    elif opcion == 2:
        print("PILAS A LAS QUE LES PUEDE ELIMINAR:")
        print(" ENCICLOPEDIA \n CUENTOS \n OTROS \n PILA1 \n PILA2")
        print("---- F A V O R  D E  I N G R E S A R  L A  O P C I O N  E N  M A Y U S C U L A S ----")
        ingresar2=input("¿A QUE PILA DESEA ELIMINAR UN NUEVO ELEMENTO? ")

        if ingresar2 == "ENCICLOPEDIA":
            if len(enciclopedia) == 0:
                print("NO  HAY ELEMENTOS PARA ELIMINAR")
            else:
                print("EL ELEMENTO", enciclopedia.pop() ,"FUE ELIMINADO")
            main()
            
        elif ingresar2 == "CUENTOS":
            if len(cuentos) == 0:
                print("NO  HAY ELEMENTOS PARA ELIMINAR")
            else:
                print("EL ELEMENTO", cuentos.pop() ,"FUE ELIMINADO")
            main()

        elif ingresar2 == "OTROS":
            if len(otros) == 0:
                print("NO  HAY ELEMENTOS PARA ELIMINAR")
            else:
                print("EL ELEMENTO", otros.pop() ,"FUE ELIMINADO")
            main()

        elif ingresar2 == "PILA1":
            if len(pila1) == 0:
                print("NO  HAY ELEMENTOS PARA ELIMINAR")
            else:
                print("EL ELEMENTO", pila1.pop() ,"FUE ELIMINADO")
            main()

        elif ingresar2 == "PILA2":
            if len(pila2) == 0:
                print("NO  HAY ELEMENTOS PARA ELIMINAR")
            else:
                print("EL ELEMENTO", pila2.pop() ,"FUE ELIMINADO")
            main()

        else:
            print("INTENTELO DE NUEVO")
            main()

    #OPCION 3 MOSTRAR PILA
    if opcion == 3:
        print("PILAS DISPONIBLES PARA MOSTRAR:")
        print(" ENCICLOPEDIA \n CUENTOS \n OTROS \n PILA1 \n PILA2")
        print("---- F A V O R  D E  I N G R E S A R  L A  O P C I O N  E N  M A Y U S C U L A S ----")
        mostrar=input("¿QUE PILA DESEA MOSTRAR? ")
        if mostrar == "ENCICLOPEDIA":
            print(enciclopedia)
            print("")
            main()

        elif mostrar == "CUENTOS":
            print(cuentos)
            print("")
            main()

        elif mostrar == "OTROS":
            print(otros)
            print("")
            main()

        elif mostrar == "PILA1":
            print(pila1)
            print("")
            main()

        elif mostrar == "PILA2":
            print(pila2)
            print("")
            main()

        else:
            print("INTENTELO DE NUEVO")
            main()

    #OPCION 4 TAMAÑO DE LA PILA
    if opcion == 4:
        print("PILAS DISPONIBLES:")
        print(" ENCICLOPEDIA \n CUENTOS \n OTROS \n PILA1 \n PILA2")
        print("---- F A V O R  D E  I N G R E S A R  L A  O P C I O N  E N  M A Y U S C U L A S ----")
        tamaño=input("¿DE QUE PILA DESEA MOSTRAR EL NUMERO DE LIBROS? ")
        if tamaño == "ENCICLOPEDIA":
            print(len(enciclopedia))
            print("")
            main()

        elif tamaño == "CUENTOS":
            print(len(cuentos))
            print("")
            main()

        elif tamaño == "OTROS":
            print(len(otros))
            print("")
            main()

        elif tamaño == "PILA1":
            print(len(pila1))
            print("")
            main()

        elif tamaño == "PILA2":
            print(len(pila2))
            print("")
            main()

        else:
            print("INTENTELO DE NUEVO")
            main()

    #OPCION 5 PARA SALIR
    if opcion == 5:
        exit()
    else:
        print("OCURRIO UN ERROR, INTENTELO DE NUEVO")
        main()
main()