#Bucles IV Parte 2

import  math

print("Programa de calculo de raíz cuadrada")
numero=float(input("Introduce un número:\n"))

intentos=0

while numero<0:
	print("No se puede hallar la raíz cuadrada de un número negativo")

	if intentos==2:
		print("Has consumido muchos intentos. El programa ha finalizado")
		break;

	num=float(input("Introduce un número:\n"))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero) #Clase math
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))
