lista=[]
lista2=[]
head=None
cola=None
sig=None
class Circular:
    def __init__(self):
        pass

    def siguiente(self,elemento):
        tam=len(lista)
        if tam==0:
            sig=None
        else:
            for i in range(0,tam):
                if lista[i]==elemento and i!=(tam-1):
                    sig=lista[i+1]
                    break
                elif lista[i]==elemento and i==(tam-1):
                    sig=lista[0]
                    break
                else:
                    sig="estacion no encontrada"
        return sig

    def siguiente2(self,pos):
        tam=len(lista2)
        pos=pos-1
        if tam==0:
            sig=None
        else:
            if (pos==(tam-1)):
                sig=lista2[0]
            else:
                sig=lista2[pos+1]
        return sig
        
    def insertarFinal(self,elemento):
        tam=len(lista)
        if tam==0:
            lista.append(elemento)
            head=elemento
            cola=elemento
            sig=elemento
        else:
            lista.append(elemento)
            head=lista[0]
            cola=elemento
            sig=self.siguiente(elemento)
        return head,cola,sig


    def insertarFinal2(self,elemento):
        tam=len(lista2)
        if tam==0:
            lista2.append(elemento)
            head=elemento
            cola=elemento
            sig=elemento
        else:
            lista2.append(elemento)
            head=lista2[0]
            cola=elemento
            sig=self.siguiente(elemento)
        return head,cola,sig


    def insertarPosicion(self,elemento,pos):
        if pos==0:
            print("no hay posicion 0, supongo que elegiste la 1")
        else:
            pos=pos-1

        tam=len(lista)
        if (tam==0 and pos>0):
            print("la lista esta vacia por lo que el elemento se insertara al incio")
            self.insertarInicio(elemento)
        elif(tam==0 and pos==0):
            self.insertarInicio(elemento)
        elif(tam>0 and pos<=tam):
            lista.insert(pos,elemento)
            print(lista)
        else:
            print("imposible, posicion no encontrada")
    
    def insertarPosicion2(self,pos,elemento):
        if pos==0:
            print("no hay posicion 0, supongo que elegiste la 1")
        else:
            pos=pos-1

        tam=len(lista2)
        if (tam==0 and pos>0):
            print("la lista esta vacia por lo que el elemento se insertara al incio")
            self.insertarInicio2(elemento)
        elif(tam==0 and pos==0):
            self.insertarInicio2(elemento)
        elif(tam>0 and pos<=tam):
            lista2.insert(pos,elemento)
            print(lista2)
        else:
            print("imposible, posicion no encontrada")


    def insertarInicio(self,elemento):
        tam=len(lista)
        if tam==0:
            lista.append(elemento)
            head=elemento
            cola=elemento
            sig=elemento
        else:
            lista.insert(0,elemento)
            tam=len(lista)
            head=lista[0]
            cola=lista[tam-1]
            sig=self.siguiente(elemento)
        return head,cola,sig

    def insertarInicio2(self,elemento):
        tam=len(lista2)
        if tam==0:
            lista2.append(elemento)
            head=elemento
            cola=elemento
            sig=elemento
        else:
            lista2.insert(0,elemento)
            tam=len(lista2)
            head=lista2[0]
            cola=lista2[tam-1]
            sig=self.siguiente(elemento)
        return head,cola,sig



    def eliminar(self,elem):
        tam2=1
        while (tam2>0):
            tam=len(lista)
            elim=[]
            for i in range(0,tam):
                if elem==lista[i]:
                    elim.append(i)
                else:
                    pass
            tam2=len(elim)
            if tam2>0:
                for a in range(0,tam2):
                    el=elim[0]
                    del lista[el]
            else:
                pass

    def eliminar2(self,pos):
        tam=len(lista2)
        if tam==0:
            print("no hay distancias que borrar")
        elif tam==2:
            print("no puedes borrar ")
        else:
            if pos==0 or pos==1:
                print("no se puede borrar la base")
            elif pos==tam:
                print("no se puede borrar la ultima parada de retorno")
            elif pos>tam:
                print("numero de parada no existente")
            else:
                del lista2[pos-1]

    def updatepos(self,posicion,nuevo):
        tam=len(lista)
        posicion=posicion-1
        if posicion>=tam:
            print("imposible borrar, posicion no existente")
        else:
            lista[posicion]=nuevo

    def updatepos2(self,posicion,nuevo):
        tam=len(lista2)
        posicion=posicion-1
        if posicion>=tam:
            print("imposible borrar, posicion no existente")
        else:
            lista2[posicion]=nuevo
    
    def updateval(self,valor,nuevo):
        if valor in lista:
            tam=len(lista)
            for i in range(0,tam):
                if lista[i]==valor:
                    lista[i]=nuevo
        else:
            print("valor no existe en esta ruta")

    def updateval2(self,pos,nuevo):
        tam=len(lista2)
        if pos>=tam:
            print("posicion no valida")
        else:
            print(lista2)
            lista2[pos]=nuevo
    




obj=Circular()

while True:
    print("1--estaciones")
    print("2--distancias")
    prob=int(input("Elige:"))
    while(prob<1 or prob>2):
        prob=int(input("Error,Elige:"))
        
    if prob==1:
        lista=[]
        while True:
            print("1--insertar")
            print("2--buscar siguiente estacion")
            print("3--eliminar")
            print("4--actualizar")
            option=int(input("Ingresa:"))
            while (option<1 or option>4):
                option=int(input("Error,Ingresa:"))
            if option==1:
                tam=len(lista)
                if tam==0:
                    valor=input("tu ruta esta vacia,ingresa el nombre de la primera estacion:")
                    obj.insertarInicio(valor)
                    print(lista)
                elif tam==1:
                    print("solo tienes una estacion")
                    print(lista)
                    print("la que vas a insertar,la quieres")
                    print("1--antes")
                    print("2--despues")
                    antdes=int(input("elige:"))
                    while (antdes<1 or antdes>2):
                        antdes=int(input("error,elige:"))
                    if antdes==1:
                        valor=input("ingresa el nombre de la estacion:")
                        obj.insertarInicio(valor)
                        print(lista)
                    if antdes==2:
                        valor=input("ingresa el nombre de la estacion:")
                        obj.insertarFinal(valor)
                        print(lista)
                elif tam>1:
                    print(lista)
                    print("donde quieres insertar")
                    print("1--inicio" )
                    print("2--final")
                    print("3--en una posicion especifica")
                    pos=int(input("Elige:"))
                    while (pos<1 or pos>3):
                        pos=int(input("Elige:"))
                    if pos==1:
                        valor=input("Escribe el nombre de la estacion:")
                        obj.insertarInicio(valor)
                        print(lista)
                    elif pos==2:
                        valor=input("Escribe el nombre de la estacion:")
                        obj.insertarFinal(valor)
                        print(lista)
                    else:
                        valor=input("nombre de la estacion:")
                        pos=int(input("posicion:"))
                        obj.insertarPosicion(valor,pos)
            elif option==2:
                print(lista)
                tam=len(lista)
                if tam==0:
                    print("no hay estaciones que buscar en esta ruta")
                else:
                    elem=input("escribe el nombre de la estacion anterior a la que quieres saber:")
                    sig=obj.siguiente(elem)
                    if sig!="estacion no encontrada":
                        print("la estacion siguiente es "+sig)
                    else:
                        print(sig)
            elif option==3:
                print (lista)
                tam=len (lista)
                if tam==0:
                    print("no hay estaciones que eliminar en esta ruta")
                else:
                    valor=input("ingresa el nombre de la estacion a eliminar:")
                    obj.eliminar(valor)
                    print(lista)
            elif option==4:
                print(lista)
                tam=len (lista)
                if tam==0:
                    print("no hay estaciones que actualizar en esta ruta")
                else:
                    print("actualizar por")
                    print("1--numero de posicion en la ruta")
                    print("2--nombre de la estacion")
                    borrar=int(input("elige:"))
                    while (borrar<1 or borrar>2):
                        borrar=int(input("error,elige:"))
                    if borrar==1:
                        pos=int(input("posicion:"))
                        valor=input("nuevo nombre:")
                        obj.updatepos(pos,valor)
                        print(lista)
                    else:
                        val=input("nombre de la estacion:")
                        valor=input("nuevo nombre:")
                        obj.updateval(val,valor)
                        print(lista)
            print("deseas continuar en este problema")
            print("[1]--si")
            print("[2]--no")
            dec=int(input("decision:"))
            while (dec<1 or dec>2):
                dec=int(input("decision:"))
            if dec==2:
                break        
    else:
        lista2=[]
        while True:
            print("1--insertar distancia ")
            print("2--buscar distancia desde una parada a la siguiente")
            print("3--eliminar una distancia")
            print("4--actualizar distancia")
            option=int(input("Ingresa:"))
            while (option<1 or option>4):
                option=int(input("Error,Ingresa:"))
            if option==1:
                tam=len(lista2)
                if tam==0:
                    print("tu lista con las distancias esta vacia")
                    print("primero,")
                    base=int(input("ingresa el tiempo en minutos que realiza un vehiculo de la ultima parada, a la base:"))
                    parada=int(input("ingresa el tiempo en minutos de la base a la ultima parada"))
                    obj.insertarInicio2(base)
                    obj.insertarFinal2(parada)
                    print(lista2)
                else:
                    print("tu cuentas con la base y con "+str(tam-1)+" paradas en este momento")
                    print(lista2)
                    if tam==2:
                        pos=1
                        if pos==1:
                            valor=int(input("ingresa la distancia desde la base hasta esta parada" ))
                            pos=pos+1
                            obj.insertarPosicion2(pos,valor)
                    elif tam>2:
                        pos=int(input("posicion donde ingresaras la distancia:"))
                        if pos==tam:
                            print("imposible agregar en esta posicion, es la ultima parada")
                        elif (pos==0 or pos==1):
                            print("imposible agregar en esta posicion, es la base")
                        else:
                            if pos>tam:
                                print("la posicion excede la cantidad de registros")
                            else:
                                valor=int(input("ingresa la distancia desde la parada"+str(pos-1) +" hasta esta parada:" ))
                                obj.insertarPosicion2(pos,valor)
                                act=int(input("ingresa la distancia desde la actual parada"+str(pos)+"hasta la actual parada"+str(pos+1)))
                                obj.updateval2(pos,act)
                                print(lista2)
            elif option==2:
                print(lista2)
                pos=int(input("numero de parada que quiere saber la distancia de su siguiente:"))
                distancia=obj.siguiente2(pos)
                if pos==1:
                    print("desde la base tu tardas "+str(distancia)+" minutos para llegar a la parada "+str(pos+1))

                else:
                    if (pos==(len(lista2))):
                        print("desde la parada "+str(pos)+" tu tardas "+str(distancia)+" minutos para llegar a la base")

                    else:
                        print("desde la parada "+str(pos)+" tu tardas "+str(distancia)+" minutos para llegar a la "+str(pos+1))

            elif option==3:
                pos=int(input("numero de parada a eliminar:"))
                ant=pos-1
                sig=pos
                obj.eliminar2(pos)
                if pos!=1:
                    if (sig==(len(lista2))):
                        valor=int(input("nueva distancia de la parada "+str(ant)+"a la ultima parada"))
                    else:
                        valor=int(input("nueva distancia de la parada "+str(ant)+"a la "+str(sig)))
                    obj.updateval2(sig,valor)
                print(lista2)
            elif(option==4):
                tam=len(lista2)
                if tam==0:
                    print("no hay que actualizar")
                elif tam==2:
                    print("solo hay 2 registros la base, y la ultima parada no se pueden modificar las distancias")
                else:
                    pos=int(input("posicion a actualizar:"))
                    if (pos==0 or pos==1):
                        print("no se puede actualizar la distancia de la ultima parada a la base")
                    if pos==tam:
                        valor=int(input("ingresa el nuevo valor:"))
                        obj.updateval2(pos,valor)
                    elif pos>1 and pos<tam:
                        valor=int(input("tiempo desde la parada "+str(pos-1)+" hasta la "+str(pos)))
                        valor2=int(input("tiempo desde la parada "+str(pos)+" hasta la "+str(pos+1)))
                        obj.updateval2(pos,valor)
                        obj.updateval2((pos+1),valor2)
                    print(lista2)


            print("deseas continuar en este problema")
            print("[1]--si")
            print("[2]--no")
            dec=int(input("decision:"))
            while (dec<1 or dec>2):
                dec=int(input("decision:"))
            if dec==2:
                break 

    print("¿salir?")
    print("[1]--si")
    print("[2]--no")
    salir=int(input("decision:"))
    while (salir<1 or salir>2):
        salir=int(input("decision:"))
    if salir==1:
        break     