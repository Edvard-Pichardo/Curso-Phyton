#Excepciones I (Video 21)

#Son errores que ocurren durante la ejecución del programa.
#La sintaxis puede estar correcta pero durante la ejecución ocurrió algo inesperado

#Se necesita hacer una captura/control de excepciones con try y except

#Sintaxis:
# try:
#    cuerpo del try
# except nombre_del_error:
#    cuerpo del except



def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:		
		return num1/num2

	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operación errónea"

while True:	
	try: 
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break
	except ValueError:
		print("Los valores introducidos no son correctos. Intentalo nuevamente.")		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")