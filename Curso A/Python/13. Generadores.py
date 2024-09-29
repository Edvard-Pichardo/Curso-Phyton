#Generadores
#Estructuras que extraen valores deuna función y se almacenan en objetos iterables (se pueden recorrer).
#Se almacenan de uno en uno.
#El valor permanece en un estado de pausa hasta que se solicita el siguiente.

#Son más eficientes que lasfunciones tradicionales.
#Muy útiles con listas de valores infinitos.
#Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno.

#yield nombre

print("Programa que haceuna lista de números pares.")


#def generaPares(limite):
#	num=1
#	miLista=[]
#	while num<limite:
#		miLista.append(num*2)
#		num=num+1
#	return miLista
#print(generaPares(10))


def generaPares2(limite):
	num=0
	while num<limite:
		yield num*2
		num=num+1

devuelvePares=generaPares2(10)

#for i in devuelvePares:
#	print(i)

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))
