class Node:
    #Metodo para inicializar un nodo, crea un nodo y un apuntador a none
    def __init__(self, Value):
        self.Value = Value
        self.Next = None

    #Creacion del metodo str para converir a str el valor ingresado por el usuario
    def __str__(self):
        return str(self.Value)


class LinkedList:

    #Metodo para crear una lista, sin valores y con longitud 0
    def __init__(self):
        self.First = None  #Lista vacia
        self.Size = 0  #Longitud es 0

    #Metodo append (Aqui se muestra como funciona el metodo de las listas)
    def Append(self, Value):
        MyNode = Node(Value)  #Se crea un nodo y nosotros le asignamos el valor
        if self.Size == 0:  #Si el tamaño de la lista inicia en 0 en esa posicion se va a asignar el primer valor
            self.First = MyNode  #Primera inserción en la lista
        else:
            Current = self.First  #Si ya existe un valor asignado a la posicion 0
            while  Current.Next != None:  #Mientras la posicion actual del nodo sea dif a "None" continuará el recorrido
                Current = Current.Next  #La posicion actual es en el primer nodo (Posicion 0)
            Current.Next = MyNode  #Al nuevo nodo se le asigna el valor introducido por el usuario

        self.Size += 1  #Crece el tamaño de la lista en 1
        return MyNode

    def Remove(self, Value):

        if self.Size == 0:  #Si se busca remover algo de una lista vacia se regresa un error del tipo IndexError
            return IndexError
        else:
            Current = self.First  #Nos posicionamos en el primer nodo
            try:
                while Current.Next.Value != Value:  #Mientras el valor del proximo nodo sea diferente al valor asignado por el usuario
                    if Current.Next == None:  #Si el siguiente nodo es "None" regresa un error del tipo IndexError
                        return ValueError
                    else:
                        Current = Current.Next  #De lo contrario continua el recorrido, cambiando al siguiente nodo
            except AttributeError:  #No se por que da un error del tipo
                return False

            DeletedNode = Current.Next  #El nodo a borrar es el proximo al que estamos posicionados actualmente
            Current.Next = DeletedNode.Next  #se corta la conexion del nodo actual con el borrado (La siguiente posicion despues
                                             #del nodo actual sera la posicion despues del nodo borrado)
        self.Size -= 1  #Se le resta uno al tamaño de la lista
        return DeletedNode

    def __len__(self):
        return self.Size  #El metodo len le "Asigna" la longitud a la lista

    def __str__(self):
        #Con este metodo str se crea la estructura para imprimir
        String = "["  #Toda lista inicia con corchetes
        Current = self.First  #Se agrega el primer valor de la lista
        for i in range(len(self)):  #Iniciamos el recorrido de la lista hasta llegar al tamaño de la misma
            String += str(Current)  #A la cadena final se le concatena el valor del nodo actual
            if i != len(self) - 1:  #Mientras el nodo actual no sea el ultimo se concatenará una coma
                String += str(", ")
            Current = Current.Next  #Avanzamos una posicion en la lista
        String += "]"  #Cuando el recorrido llegue al final se concatena el ultimo corchete
        return String

MyList = LinkedList()
lista = ["Compañeros"]

print("")
print("|================| L I S T A   O R I G I N A L |================|")
MyList.Append("Hola")
MyList.Append(lista)
MyList.Append("De TIC")
MyList.Append(41)
print("")

print(MyList)

print("")
print("|==============| L I S T A   M O D I F I C A D A |==============|")
MyList.Remove("De TIC")
MyList.Remove(41)
print("")

print(MyList)

MyList.Append("Holaa")
lista.append("Hola")
print(MyList)