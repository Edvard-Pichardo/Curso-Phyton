#Ejercicio 3

a=int(input("Introduce un número positivo: "))
b=0

while a>=0:
	b=b+a
	a=int(input("Escribe otro número positivo: "))

print("No aceptamos números negativos.")
print("La suma de todos los números positivos introducidos es de "+ str(b))