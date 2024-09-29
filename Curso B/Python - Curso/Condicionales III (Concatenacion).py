#Condicionales III

#Concatenacióran de operadores de operación
#Switch, opedores and y or, operador in

#atajo para abrir consola: alt+b
#Para cerrar consola: ctrol+w


# Programa para evaluar la veracidad de una edad

#edad=int(input("Introduce una edad:\n"))
#
#if 0<edad<100: #Concatena operadores de operación, lo que permite utilizar varias comparaciones en un mismo if
#	print("La edad es correcta")
#else:
#	print("Edad incorrecta")




#Programa para evaluar salarios

salario_presidente=int(input("Introduce el salario del presidente:\n"))
print("Salario presidente: $" + str(salario_presidente))

salario_director=int(input("Introduce el salario del director:\n"))
print("Salario director: $" + str(salario_director))

salario_jefe=int(input("Introduce el salario del jefe:\n"))
print("Salario jefe: $" + str(salario_jefe))

salario_adm=int(input("Introduce el salario del administrativo:\n"))
print("Salario administrativo: $" + str(salario_adm))

if salario_adm<salario_jefe<salario_director<salario_presidente:
	print("Todo está en orden")
else:
	print("Algo está fallando")
