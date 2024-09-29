#POO IV #Constructor, estado incial y encapsulamiento

class coche():
	
	def __init__(self):
		self.__largoChasis=250  #Estado inicial (de fábrica) y lo denominamos con un constructor (nos dice claramente cuál es el estado incial que tienenlos objetos en común de esa clase) 
		self.__anchoChasis=120
		self.__ruedas=4  #Está encapsulada con dos guines bajos
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			return("El coche está en marcha") 
		else:
			return("El coche está parado")


	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
			self.__largoChasis, ".")


miCoche=coche() 

print(miCoche.arrancar(True))
miCoche.estado()


print("----------A continuación vamos a crear el segundo objeto---------------")


miCoche2=coche()

print(miCoche2.arrancar(False))
miCoche2.__ruedas=2

miCoche2.estado()



