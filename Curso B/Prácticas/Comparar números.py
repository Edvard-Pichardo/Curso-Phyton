#Comparar números

print("Este programa compara dos números y devuelve el mayor de ellos")

a=int(input("Introduce el primer número: "))
b=int(input("Introduce el segundo número: "))

def NumMax(num1, num2):
	if num1<num2:
		print("El número mayor es: ", num2)
	elif num2<num1:
		print("El número mayor es: ", num1)
	else:
		print("Los números son iguales")


NumMax(a,b)