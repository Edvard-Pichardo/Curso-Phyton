#Herencia

#La herencia se usa para reutilizar códigos para crear objetos similares.
#Se puede utilizar paracaracteristicas y comportamientos en común.
#Se trata de construir una unica clase con todas las propiedades y metodos de cada una de lassubclases y luego especificarlos en su propias clases.
#A esta clase se le denomina "Clase padre" o "superclase".

class vehiculos():
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
		self.frenta=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)


class Moto(vehiculos):
	pass

miMoto=Moto("Nissan", "AG95")

miMoto.estado()

miMoto.arrancar()

miMoto.estado()



