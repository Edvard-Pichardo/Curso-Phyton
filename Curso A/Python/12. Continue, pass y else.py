#Continue, pass and else

#Continue salta a la siguiente interación de bucle
#Pass devuelve null en el interior de un bucle
#Else de lo contrario

#for letra in "Python":
#	if letra=="h":
#		continue
#	print("Estamos viendo la letra: "+ letra)


nombre=input("Introduce una frase: ")
contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1



print("Hay "+str(contador)+" letras en: "+ nombre)

#while True:
#	pass

#class MiClase:
#	pass #Para implementar más tarde

email=input("Escribe un correo electronico: ")

for j in email:
	if j=="@":
		arroba=True
		break;
else: #Se ejecuta cuando el bucle este vacío y termine.
	arroba=False

print(arroba)



