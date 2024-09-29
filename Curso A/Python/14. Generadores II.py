#Generadores II

#yield from: Simplifica el código en bucles anidados dentro de un generador

#def devuelveCiudades(*ciudades): #* va a recibir un número indeterminado de elementos en forma de tupla
#	for elemento in ciudades:
#		yield elemento
#
#ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
#
#print(next(ciudades_devueltas))
#print(next(ciudades_devueltas))



#def devuelveCiudades(*ciudades): #* va a recibir un número indeterminado de elementos en forma de tupla
#	for elemento in ciudades:
#		for subElemento in elemento:
#			yield subElemento
#
#ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
#
#print(next(ciudades_devueltas))
#print(next(ciudades_devueltas))



def devuelveCiudades(*ciudades): #* va a recibir un número indeterminado de elementos en forma de tupla
	for elemento in ciudades:
		#for subElemento in elemento:
		yield from elemento #Simplifica el bucle for anidado

ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
