#Excepciones III Lanzar excepciones
#Instrucción Raise

def eEdad(edad):

	if edad<0:
		raise TypeError("No se permiten edades negativas prro")
	elif edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres casi viejo"
	elif edad<100:
		return "Eres viejo"
	else:
		return "Cuidate..."
	
print(eEdad(-10))

print("Esta linea de código no saldrá si hay una edad negativa")


