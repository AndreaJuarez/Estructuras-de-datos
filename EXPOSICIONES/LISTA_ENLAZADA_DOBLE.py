class Nodo:
    def __init__(self,dato):
        self.siguiente=None
        self.anterior=None
        self.info=dato

    def verNodo(self):
        return self.info

class Lista:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def vacia(self):
        if self.cabeza==None:
            return True
        else:
            return False

    def InsertarPrimero(self,dato):
        temporal=Nodo(dato)
        if self.vacia()==True:
            self.cabeza=temporal
            self.cola=temporal
        else:
            temporal.siguiente=self.cabeza
            self.cabeza.anterior=temporal
            self.cabeza=temporal

    def listar(self):
        print("***listado***")
        temporal=self.cabeza
        while temporal!=None:
            print(temporal.verNodo(),end=' ')
            temporal=temporal.siguiente

    def listarDesdeCola(self):
        print("***listado***")
        temporal=self.cola
        while temporal!=None:
            print(temporal.verNodo(),end=' ')
            temporal=temporal.anterior

    def borrarPrimero(self):
        if self.vacia()==False:
            self.cabeza=self.cabeza.siguiente
            self.cabeza.anterior=None

    def borrarUltimo(self):
        if self.cola.anterior==None:
            self.cabeza=None
            self.cola=None
        else:
            self.cola=self.cola.anterior
            self.cola.siguiente=None

    def borrarPosicion(self,pos):
        anterior=self.cabeza
        actual=self.cabeza
        k=0
        if pos > 0:
            while k != pos and actual.siguiente != None:
                anterior=actual
                actual=actual.siguiente
                k+=1
            if k == pos:
                temporal=actual.siguiente
                anterior.siguiente=actual.siguiente
                temporal.anterior=anterior

listas = Lista()

case = "10"
print("Menu iniciado")
while case =="10":
    print("")
    print("---Menu de acciones---")
    print("---Escoja que hacer---")
    print("[1] Insertar elemento")
    print("[2] Mostar lista (Del primero al ultimo)")
    print("[3] Mostar lista (Del ultimo al primero)")
    print("[4] Eliminar el primer elemento de la lista")
    print("[5] Eliminar el ultimo elemento de la lista")
    print("[6] Eliminar una posicion espefifica")
    print("[0] Salir")
    print("")
    case = input("")
    print("")

    # Muestra la lista del ultimo al primero
    if case == "2":
        listas.listarDesdeCola()
        print("")
        case = "10"

    # Muestra la lista del primero al ultimo
    elif case == "3":
        listas.listar()
        print("")
        case = "10"

    # Elimina el ultimo dato insertado
    elif case == "4":
        listas.borrarPrimero()
        print("")
        case = "10"

    # Elimina el primer dato insertado
    elif case == "5":
        listas.borrarUltimo()
        print("")
        case = "10"

    # Inserta un nuevo elemento
    elif case == "1":
        print("Introdusca el elemento a insertar")
        vall=input(str(""))
        listas.InsertarPrimero(vall)
        print("")
        case = "10"

    # Inserta un nuevo elemento
    elif case == "6":
        print("Introdusca la posicion a eliminar")
        vall=input(int(""))
        listas.borrarPosicion(vall)
        print("")
        case = "10"

    elif case == "7":
        listas.borrarPosicion(2)
        print("")
        case = "10"

    # Termina el programa
    else:
        print("")
        print("Menu cerrado")
        case = 0
        print("")

print("---------------------------")
print("--- Programa finalizado ---")
print("---------------------------")
#Terminado


#listas = Lista()
#listas.InsertarPrimero(2)
#listas.InsertarPrimero(4)
#listas.InsertarPrimero(6)
#listas.InsertarPrimero(8)
#listas.listar()
# listas.listarDesdeCola()
# listas.borrarPrimero()
# listas.borrarUltimo()
# listas.borrarPosicion(2)
#listas.listar()
#listas.listarDesdeCola()