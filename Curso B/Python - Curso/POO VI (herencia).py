#POO VI
#Herencia: 
# Trasladar el comportamiento de la herencia de la vida real a código de programación

# Clase 1 = Clase Padre // Superclase
# Clase 2 = Subclase y Superclase de la clase 3, 4 y 5
# Clase 3, clase 4, clase 5

#Sirve para reutilizar código en caso de crear objetos similares
#Caracteristicas y comportamientos en común

class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo:", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos): #Aquí se ejecuta la herencia
	pass

miMoto=Moto("Honda", "CBR")	

miMoto.estado()