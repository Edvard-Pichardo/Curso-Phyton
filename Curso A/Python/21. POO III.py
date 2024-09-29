#POO III

#Sintaxis:

class coche():
	#Propiedades
	largoChasis=250  #Tiene 4 propiedades
	anchoChasis=120
	ruedas=4
	enmarcha=False

	#Comportamiento creando métodos
	def arrancar(self): #self hace referencia al propio objeto quepertenece a la clase (this---C++--Java)
		#pass impide que da error si aún no modificamos el comportamiento
		self.enmarcha=True
	def estado(self):
		if(self.enmarcha):
			return("El coche está en marcha") #Tiene 2 comportamientos
		else:
			return("El coche está parado")

#Crear objtos
miCoche=coche() #Instanciar/Ejemplarizar una clase

print("El largo del coche es: ", miCoche.largoChasis, " cm")
print("El coche tiene ", miCoche.ruedas, " ruedas")
#miCoche.arrancar()
print(miCoche.estado())


