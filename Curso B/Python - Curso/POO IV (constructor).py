#POO IV
#Constructor, estado incial, encapsulación

class Coche():

	def __init__(self): #Este es el constructor de la clase
		self.largoChasis=250 
		self.anchoChasis=120
		self.__ruedas=4  #Aquí encapsulamos la variable ruedas
		self.enmarcha=False
                                         
	def arrancar(self,arrancamos):                 
	 	self.enmarcha=arrancamos

	 	if(self.enmarcha==True):
	 		return "El coche está en marcha"
	 	else:
	 		return "El coche está detenido"


	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)



miCoche=Coche() 

#print("El largo del coche es ", miCoche.largoChasis)
#print("El cohe tiene ", miCoche.__ruedas, " ruedas")

print(miCoche.arrancar(True))
print(miCoche.estado())


print("\n--------------A continuación creamos el segundo objeto---------")

miCoche2=Coche()

#print("El largo del coche es ", miCoche2.largoChasis)
#print("El cohe tiene ", miCoche2.__ruedas, " ruedas")

miCoche2.__ruedas=1
print(miCoche2.arrancar(False))
print(miCoche2.estado())

#Estado inicial: Suele ser habitual que las caracteristicas comunes sean las de fabrica
#Las instancias dentro de esa clase tendrá dicho estado incial
#Se definen mediante un constructor

#Encapsulación: Encapsula/Protege una propiedad para que no se pueda modificar desde fuera de la clase
