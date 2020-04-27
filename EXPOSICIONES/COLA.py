class Cola():
    def __init__(self):
        self.cola = []
        self.size = 0

    def estaVacia(self):
        return self.cola == []

    def agregar(self, dato):
        self.cola += [dato]
        #self.cola = self.cola + [dato]
        self.size += 1
        #self.cola = self.cola + 1

    def eliminar(self):
        if self.estaVacia():
            print("La cola esta vacia")
        else:
            self.cola = [self.cola[i] for i in range(1,self.size)]
            self.size -= 1

    def mostrar(self):
        n = self.size - 1
        while n > -1:
            print("[%d]  =>   %d"%(n,self.cola[n]))
            n -= 1

cola = Cola()

cola.agregar(11)
cola.agregar(12)
cola.agregar(13)
cola.agregar(14)
cola.agregar(15)
cola.agregar(16)

cola.mostrar()
print("_"*18)
cola.eliminar()
cola.mostrar()