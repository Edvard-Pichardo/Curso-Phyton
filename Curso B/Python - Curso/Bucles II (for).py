#Bucles II (for)

#Recorriendo strings
#Tipo range
#Notaciones especiales con la función print

for i in [1,2,3]:
	print("Hola", end=" ") #Argumento para terminar la oración


print("\nPrograma para verificar la autenticidad de un correo")
email=False
miEmail=input("Introduce tu correo:\n")

for i in miEmail:
	if(i=="@"): #Se puede colocar argumentos dentro del if
		email=True

#if email==True:
if email:
	print("Email es correcto")
else:
    print("Email no es correcto")	


#contador
#contador=contador+1


print("\nPrograma para decir hola")

for i in range(5):
	print("Hola")

for i in range(5):
	print(i)





