#28. Polimorfismo
#Significa cambiar de forma o comportamiento

class coche():
	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")

miVehiculo=Moto()
#miVehiculo.desplazamiento()

miVehiculo2=coche()
#miVehiculo2.desplazamiento()

miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

#El método o comportamiento es el mismo
#Para hacer lo mismo utilizaremos el polimorfismo
#Presindimos el uso de todas esa instancias y creamos una función:

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()


desplazamientoVehiculo(miVehiculo)

desplazamientoVehiculo(miVehiculo2)

desplazamientoVehiculo(miVehiculo3)