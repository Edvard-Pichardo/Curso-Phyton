#Excepciones III

#Instrccíón Raise
#Creación de excepciones propias

def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas")
		#Lanza un error del tipo que desees
	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres grande"
	elif edad<100:
		return "Cuídate..."

try:
	print(evaluaEdad(-31))
except TypeError as ErrorDeNumeroNegativo: #as=como
	print(ErrorDeNumeroNegativo)

print("Programa finalizado")