#Prueba excepciones II
def divide():

	try:

		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+str(op1/op2))
	
	except ValueError:
		print("El valor introducido es erronéo.")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")	

	finally: 
		print("Calculo finalizado")



def divide2():

	try:

		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+str(op1/op2))
	
	except:
		print("Ha ocurrido un error.")

	finally: #En el finally se ejecuta siempre
		print("Calculo finalizado")



def divide3():

	try:

		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+str(op1/op2))


	finally: #En el finally se ejecuta siempre
		print("Calculo finalizado")



divide3()