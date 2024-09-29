#Bucles III (for)

#Tipo range
#Notaciones especiales con print

for i in range(5):
	print(f"Valor de la variable {i}") #f une textos con variables

for i in range(1,10): #De que número a que número va el rango
	print(f"Valor de la variable {i}")

for i in range(0,50,5): #El ultimo número va a dictar el incremento
	print(f"Valor de la variable {i}")

#Funcion len() = Devuelve la extensión de un string

valido=False
email=input("Introduce tu email:\n")

for i in range(len(email)): #len(email) nos devuelve los elementos del correo introducido
	if email[i]=="@":
		valido=True

if valido:
	print("El correo es correcto")
else:
	print("El correo es incorrecto")