"""
Andrea Sarai Juárez Munguia
TI 41
"""
import os

class Nodo:
    def __init__(self, nombre=None, habitantes=None, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.habitantes = habitantes
        self.izquierdo = izquierdo
        self.derecho = derecho

    #RETORNARA EL NOMBRE CONCATENADO CON LA CEDULA
    def __str__(self):
        return "%s %s" %(self.nombre, self.habitantes)

class arbolBinario:
    def __init__(self):
        self.raiz = None

    #M E T O D O   P A R A   A G R E G A R
    def agregarElemento(self, elemento):
        #PRIMER ELEMENTO EN INGRESAR, VA A SER LA RAIZ
        if self.raiz == None:
            self.raiz = elemento
        else:
            auxiliar = self.raiz
            padre = None
            #EL CICLO SE VA A CORRER MIENTRAS AUXILIAR NO SEA NULO
            while auxiliar != None:
                padre = auxiliar
                if int(elemento.habitantes) >= int(auxiliar.habitantes):
                    auxiliar = auxiliar.derecho
                else: 
                    auxiliar = auxiliar.izquierdo
            if int(elemento.habitantes) >= int(padre.habitantes):
                padre.derecho = elemento
            else:
                padre.izquierdo = elemento

    
    #M E T O D O S   D E   R E C O R R I D O   E N   A R B O L E S   B I N A R I O S
    def preOrden(self, elemento):
        if elemento != None:
            print(elemento)
            self.preOrden(elemento.izquierdo)
            self.preOrden(elemento.derecho)

    def postOrden(self, elemento):
        if elemento != None:
            self.postOrden(elemento.izquierdo)
            self.postOrden(elemento.derecho)
            print(elemento)

    def inOrden(self, elemento):
        if elemento != None:
            self.inOrden(elemento.izquierdo)
            print(elemento)
            self.inOrden(elemento.derecho)

    def obtenerRaiz(self):
        return self.raiz

    #M E T O D O   P A R A   B U S C A R   P O R   C E D U L A
    def buscar(self, habitantes, auxiliar):
        if auxiliar == None:
            return None
        else:
            if habitantes == auxiliar.habitantes:
               return auxiliar.habitantes
            else:
                if habitantes < auxiliar.habitantes:
                    return self.buscar(habitantes, auxiliar.izquierdo)
                else: 
                    return self.buscar(habitantes, auxiliar.derecho)


#M E N U   D E   O P C I O N E S
if __name__ == "__main__":

    #INSTANCIAR LA CLASE
    binarios = arbolBinario()

    while(True):
        #os.system("cls")
        print("|--------------------- M E N U ---------------------|")
        print("1) AGREGAR ELEMENTO")
        print("2) RECORRER POR PREORDEN")
        print("3) RECORRER POR POSTORDEN")
        print("4) RECORRER POR INORDEN")
        print("5) BUSCAR POR NUMERO DE HABITANTES")
        print("6) SALIR")

        print("")
        opcion = input("INGRESE LA OPCION: ")
        if opcion == "1":
            nombre = input("INGRESE EL NOMBRE DEL PAIS: ")
            habitantes = input("INGRESE EL NUMERO DE HABITANTES: ")
            nodo = Nodo(nombre, habitantes)
            binarios.agregarElemento(nodo)
            print("DATOS INGRESADOS CORRECTAMENTE...")
        
        elif opcion == "2":
            print("|------------- I M P R IM I E N D O   P O R   P R E O R D E N -----------------|")
            binarios.preOrden(binarios.obtenerRaiz())

        elif opcion == "3":
            print("|------------ I M P R I M I E N D O   P O R   P O S T O R D E N ---------------|")
            binarios.postOrden(binarios.obtenerRaiz())

        elif opcion == "4":
            print("|-------------- I M P R IM I E N D O   P O R   I N O R D E N ------------------|")
            binarios.inOrden(binarios.obtenerRaiz())

        elif opcion == "5":
            buscado = input("INGRESE EL NUMERO DE HABITANTES A BUSCAR: ")
            if buscado.isdigit():
                buscado = str(buscado)
                if binarios.buscar(buscado, binarios.raiz) == None:
                    print("CEDULA NO ENCONTRADA")
                else: 
                    print("CEDULA ENCONTRADA! ", binarios.buscar(buscado, binarios.raiz), "SI EXISTE!")
            else:
                print("INGRESE SOLO DIGITOS")

        elif opcion == "6":
            print("SALIENDO DEL PROGRAMA...")
            break 
        
        else: 
            print("OPCION INCORRECTA, INTENTELO DE NUEVO!")
        print()
        #os.system("pause")
print()
            
