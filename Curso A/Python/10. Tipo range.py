#Tipo range

for i in range(5):
	print(f"Valor de la variable {i}")

for j in range(8,10):
	print(f"Valor de la variable {j}")

for k in range(10,51,2):
	print(f"Valor de la variable {k}")

#Función len. Devuelve la longitud de un string

print(len("Juan"))


#Programa para revisar el @ de un correo
valido=False
email=input("Introduce tu email: ")

for l in range(len(email)):
	if email[l]=="@":
		valido=True
if valido==True:
	print("Email correcto")
else:
	print("Email incorrecto")


