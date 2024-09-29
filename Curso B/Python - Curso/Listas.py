#Listas (arrays, vectores)

#Son estructutas de datos que permiten almacenar varios valores
#Pueden guardar diferente tipos de valores
#Se pueden expandir dinámicamente añadiendo nuevos elementos

#Sintaxis
# nombreLista=[element1, element2, element3,...]

#índice: es la posición de cada elemento dentro de la lista empezando desde el 0


miLista=["Raúl", "María", "Pepe", "Marta", "Antonio"] #Lista de 5 elementos que va desde el índice 0 hasta el índice 4

print(miLista[:]) #Imprimir la lista completa

print(miLista[2]) #Imprime el elemento del índice 2
print(miLista[-2]) #Imprime el elemento del índice 2 empezando desde el final de la lista

print(miLista[0:3]) #Porción de lista [0,3)
print(miLista[:3]) #Porción de lista [0,3)
print(miLista[1:3]) #Porción de lista [1,3)
print(miLista[2:]) #Porción de lista [2,final]

miLista.append("Rodrigo") #Agrega elementos al final de la lista
print(miLista[:])

miLista.insert(0,"Felipe") #Agrega elementos a la lista en el índice indicado
print(miLista[:])

miLista.extend(["Ana", "Daniela", "Lucía"]) #Concatena dos listas
print(miLista[:])

print(miLista.index("Antonio")) #Indica en que índice se encuentra un elemento
print(miLista.index("Ana")) 

miLista.append("Ana")
print(miLista.index("Ana")) #Nos da siempre el primer elemento si existen varios en la lista

print("Pepe" in miLista) #Usa los elementos lógicos
print("García" in miLista)

miLista.extend([5, True, 23.98]) #Puede haber varios tipos de valores dentro de la lista
print(miLista[:])

miLista.remove("Felipe")#Elimina elementos de la lista
miLista.remove(5) 
print(miLista[:])

miLista.pop() #elimina el último elemento de una lista
print(miLista[:])

miLista1=["Ana", 5, "Raul", 78.4, True]
miLista2=["Sandra", "Lucía", False]

miLista3=miLista1+miLista2
print(miLista1[:])
print(miLista2[:])
print(miLista3[:])

miLista4=["Sandra", "Lucía", False]*3 #Multiplica la lista n veces
print(miLista4[:])


