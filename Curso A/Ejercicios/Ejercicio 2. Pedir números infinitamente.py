#Ejercicio 2

numero=int(input("Introduce un número cualquiera: "))
numero1=int(input("Introduce un número mayor que "+str(numero)+": "))


while numero1>numero:
	print("Perfecto, sigamos. uwu")
	numero=numero1
	numero1=int(input("Introduce un número mayor que "+str(numero)+": "))

print(str(numero1) + " no es mayor que "+str(numero))	
print("No sigues instrucciones, el programa se ha enojado contigo y ha finalizado.")

	