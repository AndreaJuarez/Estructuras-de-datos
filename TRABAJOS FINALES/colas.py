"""
PROGRAMA CON EL OBJETIVO DE AYUDAR A LA RECEPCIÓN DE UNA EMPRESA
Andrea Sarai Juárez Munguia
TI 41
"""

#from collections import deque

#CREACION DE LA COLA
cola=[]

#CREACION DEL MENU
def main():
    print("----------------------------------- B I E N V E N I D O S -----------------------------------")
    print("------------------------------- M E N U  D E  O P C I O N E S -------------------------------")
    print("1.- INGRESAR CITA NUEVA")
    print("2.- ELIMINAR CITA")
    print("3.- MOSTAR CITAS EXISTENTES EN LA COLA")
    print("4.- CITAS EXISTENTES EN LA COLA")
    print("5.- SALIR")
    opcion=int(input("INGRESE LA OPCION QUE DESEA ELEGIR: "))

    #OPCION 1 DE INGRESAR
    if opcion == 1:
        motivo=str(input("INGRESE EL MOTIVO DE LA CITA: "))
        cola.append(motivo)
        print("")
        print("¡CITA AGENDADA EXITOSAMENTE!")
        print(cola)
        print("")
        main()

    #OPCION 2 DE ELIMINAR
    elif opcion == 2:
        if len(cola) == 0:
                print("NO  HAY CITAS PARA ELIMINAR")
                print("")
                main()
        else:
            print("LA CITA: ", cola.pop(0) ,"... FUE ELIMINADA CORRECTAMENTE")
            print("")
        main()
        
    #OPCION 3 MOSTRAR COLA
    elif opcion == 3:
        print("LAS CITAS EXISTENTES EN LA COLA SON LAS SIGUIENTES:")
        print(cola)
        print("")
        main()
    
    #OPCION 4 TAMAÑO DE LA COLA
    elif opcion == 4:
        print("EL NUMERO DE CITAS EXISTENTES EN LA COLA SON LAS SIGUIENTES:")
        print(len(cola))
        print("")
        main()

    #OPCION 5 PARA SALIR
    elif opcion == 5:
        exit()
    else:
        print("OCURRIO UN ERROR, INTENTELO DE NUEVO")
        main()
main()