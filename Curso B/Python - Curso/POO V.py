#POO V

#Encapsulación de métodos
#Es hacer que un método solo sea accesible desde la propia clase y no fuera de ella
#Utilidades: 

class Coche():

	def __init__(self): 
		self.__largoChasis=250 
		self.__anchoChasis=120
		self.__ruedas=4  
		self.__enmarcha=False
                                         
	def arrancar(self,arrancamos):                 
	 	self.__enmarcha=arrancamos

	 	if(self.__enmarcha==True):
	 		chequeo=self.__chequeo_interno()


	 	if(self.__enmarcha==True and chequeo==True):
	 		return "El coche está en marcha"

	 	elif(self.__enmarcha and chequeo==False):
	 		return "Algo ha ido mal en el chequeo. No se ha podido arrancar"

	 	else:
	 		return "El coche está detenido"


	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)


	def __chequeo_interno(self):   #Esta es una encapsulación de métodos
		print("Realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False



miCoche=Coche() 

print(miCoche.arrancar(True))
print(miCoche.estado())
#print(miCoche.chequeo_interno()) #Esto no tiene sentido


print("\n--------------A continuación creamos el segundo objeto---------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
print(miCoche2.estado())
