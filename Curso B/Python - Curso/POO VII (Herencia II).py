#POO VII (Herencia II) Video 30


#Sobreescritura de métodos
#Herencia simple y herencia múltiple

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



class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"



class Moto(Vehiculos): #Aquí se ejecuta la herencia
	hcaballito=""

	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self): #Sobreescritura de métodos
		print("Marca: ", self.marca, "\nModelo:", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


class VElectricos():
	def __init__(self):
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True


class BicicletaElectrica(VElectricos, Vehiculos): #Herencia múltiple
	pass   #El constructor heredado es el primero quese coloca




miMoto=Moto("Honda", "CBR")	

#miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangao")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici=BicicletaElectrica()
