#Operadores lógicos

print("Evaluación de salario")

salario_presidente=int(input("Introduce salario del presidente: "))
print("Salario del presidente: "+ str(salario_presidente))


salario_director=int(input("Introduce salario del director: "))
print("Salario del director: "+ str(salario_director))


salario_jefe_area=int(input("Introduce salario del jefe de área: "))
print("Salario del jefe de área: "+ str(salario_jefe_area))


salario_adm=int(input("Introduce salario del trabajador administrativo: "))
print("Salario del administrativo: "+ str(salario_adm))

if salario_adm<salario_jefe_area<salario_director<salario_presidente:
	print("Todo está en orden")
else:
	print("Algo está fallando en esta empresa")

