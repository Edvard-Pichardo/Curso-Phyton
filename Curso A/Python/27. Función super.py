#Función super()

class Persona():
	def __init__(self, nombre, edad, lugar):

		self.nombre=nombre
		self.edad=edad
		self.lugar=lugar

	def descripción(self):
		print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de residencia: ", self.lugar)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombree, edade, lugare):

		super().__init__(nombree, edade, lugare)

		self.salario=salario
		self.antiguedad=antiguedad

	def descripción(self):
		super().descripción()
		print("Salario: ",self.salario, "\nAntiguedad: ",self.antiguedad)

Antonio=Empleado(1500, 15, "Antonio", "55 años", "España")
Antonio.descripción()

print(isinstance(Antonio, Empleado))
print(isinstance(Antonio, Persona))

Manuel=Persona("Manuel", "55 años", "España")
Manuel.descripción()

print(isinstance(Manuel, Persona))
print(isinstance(Manuel, Empleado))




#Principio de sustitución "es siempre un/a": Un empleado siempre es una persona pero una persona no es siempre una persona
#isinstance devuelve true o false
