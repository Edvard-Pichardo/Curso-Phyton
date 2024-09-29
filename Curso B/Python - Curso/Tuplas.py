#Tuplas

#Estructuras parecidas a las listas
#Son listas inmutables, pues no se puede modificar (añadir, eliminar, mover)
#Permiten busquedas con el método index
#Pero permiten extraer porciones, lo que crea una nueva tupla
#Permite comprobar si un elemento se encuentra dentro de una tupla

#Ventajas:
#Son más rápidas, ocupan menos espacio, formatean strings y pueden utilizarse como claves en un diccionario (las listas no)

#Sintaxis
# nombreTupla=(element1, element2, element3, ...)

#Tiene el mismo índice que empieza desde el 0 hasta n

miTupla=("Juan", 15, "minombre", "Pedro", 15, 15)
print(miTupla[2])
print(miTupla[1])

miLista=list(miTupla) #Convierte tuplas en listas
print(miLista)
print(miTupla)

miLista1=["Juan", 15, "minombre", "Pedro"] #Convierte listas en tuplas
miTupla1=tuple(miLista1) 
print(miTupla1)

print("Juan" in miTupla) #Comprobar si un elemento está en la tupla
print(23 in miTupla)

print(miTupla.count(15)) #Cuenta cuantás veces aparece un elemento en la tupla

print(len(miTupla)) #Determina cuantos elementos están en la tupla

miTupla3=("Juan",) #Tupla unitaria
print(len(miTupla3))

miTupla4="Juan", 13, 45, "Maria" #Empaquetado de tupla
print(miTupla3)

miTupla5=("Juan", 13, 1, 1995) #Desempaquetado de tupla
nombre, dia, mes, agno=miTupla5
print(nombre)
print(dia)
print(agno)
print(mes)

