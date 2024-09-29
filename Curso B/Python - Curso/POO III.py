#POO III (vídeo 26)

#Objeto: estado, propiedades, comportamiento

class Coche():
	largoChasis=250 #Propiedades de la clase Coche
	anchoChasis=120 #Todos los objetos que pertenezcan a esta clase tendrán estas propiedades
	ruedas=4
	enmarcha=False
                                         #self está dirigido al objeto perteneciente a la clase
	def arrancar(self):                  #Se crea un método: Una función especial que pertenece a la clase que se está creando
	 	self.enmarcha=True               #Este es un comportamiento de la clase

	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está detenido"



miCoche=Coche() #Se crea el primer objeto que pertenece a la clase Coche(). Instanciar una clase.

print("El largo del coche es ", miCoche.largoChasis)
print("El cohe tiene ", miCoche.ruedas, " ruedas")

print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())

#La clase coche tiene 4 propiedades y 2 comportamientos
#Además, definimos un on¿bjeto


#Proxima clase: Estado inicial del objeto y encapsulamiento