#Generadores II (yiel from)

#Simplifica el código de los generadores en el caso de utilizar bucles anidados dentro de ese generador

def devuelve_ciudades(*ciudades):  #El asterisco hace que pueda recibir un número indeterminado de argumentos y los recibe en forma de tupla
	#for elemento in ciudades:
	#	for subelemento in elemento:
	#		yield subelemento

	for elemento in ciudades:
		yield from elemento



ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))





