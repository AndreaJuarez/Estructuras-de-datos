#Programa de almacen

class Pila:

    def __init__(self):
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self,x):
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
    #"Devuelve el elemento tope y lo elimina de la pila Si la pila está vacía levanta una excepción"
        if True:
            print("Operacion ejecutada con exito")
        try:
            return self.items.pop()
        except IndexError:
            print("La pila está vacía")

    def tam(self):
        print("----TOTAL DE PRODUCTOS EN EL ALMACEN----- ")
        print(len(self.items))

    def listar(self):
        print("----PRODUCTOS EN EL ALMACEN-----")
        print(self.items)

    def es_vacia(self):
        return self.items == []

pila=Pila()
print("-----------------PROGRAMA DE ALMACEN-------------")
#SE CREA MENU 
case = "10"
while case =="10":
    print("")
    print("-------MENU------")
    print("---Escoja que desea realizar---")
    print("[1] Insertar Producto")
    print("[2] Eliminar Producto")
    print("[3] Mostar todos los productos")
    print("[4] Muestra el total de productos que hay en el almacen")
    print("[0] Salir")
    print("")
    case = input("")
    print("")

    # Inserta un nuevo elemento
    if case == "1":
        print("Introdusca el nombre del producto:")
        vall=input(str(""))
        pila.apilar(vall)
        print("")
        case = "10"

        # Elimina el ultimo dato insertado
    elif case == "2":
        pila.desapilar()
        print("")
        case = "10"

        # Muestra todos los productos
    elif case == "3":
        pila.listar()
        print("")
        case = "10"

     # Muestra el total de productos
    elif case == "4":
        pila.tam()
        print("")
        case = "10"

     # Termina el programa
    else:
        print("")
        print("Menu cerrado")
        case = 0
        print("")

print("------ Programa finalizado ------")
#Terminado