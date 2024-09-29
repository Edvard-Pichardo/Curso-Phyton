#Generadores I

#Son estructuras que extraen valores de una función que se almacenan en objetos iterables (que se pueden recorrer)
#Se almacenen de uno en uno
#Cada vez que el generador almacena un valor, permanece pausado hasta que se solicita el siguiente. "Suspención de estado"

#Utilidad:
#Son más eficientes que las funciones tradicionales
#Son muy ´´utiles con listas de valores infinitos
#Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno

#Sintaxis:

#del nombre():
#   cuerpo del generador
#   yield nombre

def generaPares1(limite):
	num=1
	miLista=[]

	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista

print(generaPares1(10))


def generaPares(limite):
	num=1

	while num<limite:
		yield num*2
		num+=1

devuelvePares=generaPares(10)

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))	
print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))	