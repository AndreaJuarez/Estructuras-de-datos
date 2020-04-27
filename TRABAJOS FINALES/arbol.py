"""
Andrea Sarai Juárez Munguia
TI 41
"""
from collections import deque 

#INICIO
class Arbol:
    def __init__(self, elemento):
        self.elemento = elemento
        self.hijos = []

#----------------------------------------- M E T O D O S ----------------------------------------------

#METODO PARA AGREGAR ELEMENTOS
def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre)
    subarbol.hijos.append(Arbol(elemento))

def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        encontrado = buscarSubarbol(subarbol, elemento)
        if encontrado != None:
            return encontrado
    return None 

#RECORRIDO POR PROFUNDIDAD Y GRADO
#1 + la profundidad del hijo más profundo
def profundidad(arbol):
    if len(arbol.hijos) == 0:
        return 1
    profundidades = map(profundidad, arbol.hijos)
    return 1 + max(profundidades)
#maximo entre la cantidad de sus hijos y el grado de sus hijos
def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])


#EJECUCION DE RECORRIDOS
#Profundidad
def ejecutarProfundidad(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidad(hijo, funcion)
#Ancho
def ejecutarAncho(arbol, funcion, cola = deque()):
    funcion(arbol.elemento)
    if (len(arbol.hijos) > 0):
        cola.extend(arbol.hijos)
    if (len(cola) != 0):
        ejecutarAncho(cola.popleft(), funcion, cola)                                               

#IMPRIMIR
def printElemento(element):
    print(element)

familia = "Munguia Reynoso"
hermano1 = "Noemi"
hermano2 = "Saul"
hermano3 = "Aide"
hijo1 = "Miguel"
hijo2 = "Andrea"
primo1 = "Felipe"
primo2 = "Giovanni"
primo3 = "Luis"
primo4 = "Brenda"

arbol = Arbol(familia)
#ARBOL || ELEMENTO || PADRE
agregarElemento(arbol, hermano1, familia)
agregarElemento(arbol, hermano2, familia)
agregarElemento(arbol, hermano3, familia)
agregarElemento(arbol, hijo1, hermano1)
agregarElemento(arbol, hijo2, hermano1)
agregarElemento(arbol, primo1, hermano3)
agregarElemento(arbol, primo2, hermano3)
agregarElemento(arbol, primo3, hermano3)
agregarElemento(arbol, primo4, hermano3)

print(profundidad,arbol)
print(grado,arbol)

opcion=input("¿DESEA MOSTRAR LA OPCIÓN PROFUNDIDAD O LA OPCIÓN ANCHO? ")
if opcion == "profundidad":
    #PROFUNDIDAD
    ejecutarProfundidad(arbol, printElemento)
elif opcion == "ancho":
    #ANCHO
    ejecutarAncho(arbol, printElemento)
else:
    print("OPCIÓN INCORRECTA!")
