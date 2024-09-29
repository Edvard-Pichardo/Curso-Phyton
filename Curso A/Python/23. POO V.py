#POO V #Encapsulación de métodos

class coche():
	
	def __init__(self):
		self.__largoChasis=250  
		self.__anchoChasis=120
		self.__ruedas=4  
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if (self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return("El coche está en marcha") 
		elif (self.__enmarcha and chequeo==False):
			return("Algo ha ido mal en el chequeo, no podemos arrancar")
		else:
			return("El coche está parado")


	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
			self.__largoChasis)

	def __chequeo_interno(self): #Encapsular métodos
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False





miCoche=coche() 

print(miCoche.arrancar(True))
miCoche.estado()


print("----------A continuación vamos a crear el segundo objeto---------------")


miCoche2=coche()

print(miCoche2.arrancar(False))
miCoche2.estado()

#Encapsular métodos cuando la clase así lonecesite y depende de que necesita esa clase según el criterio del programador
#Si se necesita que ese objeto funcione entonces se podrá encapsular o no. 