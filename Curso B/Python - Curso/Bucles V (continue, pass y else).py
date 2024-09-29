#Bucles V (continue, pass y else)

#continue: Ignora la vuelta de bucle y salta a la siguiente
#pass: Devuelve null dentro de un bucle
#else: Por el contrario

for i in "Python":
	print("Vemos la letra: " + i)


for i in "Python":
	if i=="h":
		continue
	print("Vemos la letra: " + i)

nombre="Pildoras Informaticas"
contador=0

for i in nombre:

	if i==" ":
		continue
	
	contador+=1

print(len(nombre))
print(contador)

#while True:
#	pass

#class Miclase:
#	pass

#def miFuncion():
#	pass #Para implementar más tarde



mail=input("Escribe tu dirección de correo eléctronico:\n")

for i in mail:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False

print(arroba)