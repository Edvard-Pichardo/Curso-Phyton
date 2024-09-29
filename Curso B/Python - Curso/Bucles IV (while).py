#Bucles IV (while)

#Es un bucle indeterminado porque no sabemos cuantas veces se va a ejecutar cuando miramos el código
#while = mientras...


#Sintaxis

#while condición:
#     cuerpo del while


i=1

while i<=4:
	print("Ejecución "+ str(i))
	i=i+1

print("Terminó la ejecución")

edad=int(input("Introduce una edad:\n"))

while (edad<0 or edad>100):
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("Introduce una edad:\n"))

print("Gracias por colaborar. :3")
print("Edad del aspirante: " + str(edad))