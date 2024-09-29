#Programa de raíz cuadrada

import math

def cRaiz(num1):
	if num1<0:
		raise ValueError("El número no puede ser negativo prro xdxdxd")
	else:
		return math.sqrt(num1)

op1=int(input("Introduce un número: "))

try:
	print(cRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)


print("Programa terminado.")