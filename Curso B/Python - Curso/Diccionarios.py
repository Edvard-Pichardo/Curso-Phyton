#Diccionarios

#Son estructuras de datos que permiten almacenar datos de diferente tipo e incluso listas u otros diccionarios
#Los datos se almacenan asociados a una clave tq se crean una asociación tipo: clave-valor para cada elemento almacenado
#Los datos almacenados no están ordenados
#El orden es indiferente a la hora de almacenar información en un diccionario


#clave-valor
miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid", "México":"México"}
print(miDiccionario["Francia"]) #A cada clave se le asigna un valor
print(miDiccionario["España"])

print(miDiccionario)


miDiccionario["Italia"]="Lisboa"  #Agregar nuevos elementos al diccionario
print(miDiccionario)

miDiccionario["Italia"]="Roma" #Modifica o sobreescribe elementos
print(miDiccionario)

del miDiccionario["Reino Unido"] #Elimina elementos del diccionario
print(miDiccionario)

MiDic1={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(MiDic1)

miTupla=["España", "Francia", "Reino Unido", "Alemania"]
miDic={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}
print(miDic)
print(miDic["Francia"])


miDiccionario1={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario1)
print(miDiccionario1["Equipo"])
print(miDiccionario1["Anillos"])


miDiccionario2={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(miDiccionario2)


print(miDiccionario2.keys())
print(miDiccionario2.values())
print(len(miDiccionario2))


