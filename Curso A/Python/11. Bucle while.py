#Bucle while


#i=1

#while i<=10:
#	print("Ejecución: "+str(i))
#	i=i+1

#print("Terminó la ejecución")




#edad=int(input("Introduce tu edad: "))

#while (edad<0 or edad>100):
#	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
#	edad=int(input("Introduce tu edad: "))
#print("Gracias por colaborar. Puedes pasar.")
#print("Edad del aspirante: "+ str(edad)+ " años")


import math
print("Programa de cálculo de raíces cuadradas")
numero=int(input("Introduce el número: "))

intentos=0

while numero<0:
	print("No se puede hallar la raíz de un número negativo")
	if intentos==2:
		print("Has usado demasiados intentos, el programa se ha apagado.")
		break; #Sale del if y sigue con el programa
	numero=int(input("Introduce un número: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de "+ str(numero)+" es "+ str(solucion))
