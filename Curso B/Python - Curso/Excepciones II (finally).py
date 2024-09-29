#Excepciones II

#Clausula finally

def divide():
	while True:
		try:
			op1=float(input("Introduce el primer número: "))
			op2=float(input("Introduce el segundo número: "))
			print("La división es: "+ str(op1/op2))
			break
		except ValueError:
			print("El valor introducido es incorrecto.")
		except ZeroDivisionError:
			print("No se puede dividir entre 0.")

		finally:  #Hace que el código dentro de la instrucción se ejecute siempre
			print("Cálculo Finalizado")

def divide2():
	while True:
		try:
			op1=float(input("Introduce el primer número: "))
			op2=float(input("Introduce el segundo número: "))
			print("La división es: "+ str(op1/op2))
			break
		except:
			print("Ha ocurrido un error")

	print("Cálculo Finalizado")

divide()
#divide2()
