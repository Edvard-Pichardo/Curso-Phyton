#Evaluar la seguridad de una contraseña

print("Para tener una contraseña segura deberá tener más de 8 caracteres y sin espacios en blanco ")
password=input("Introduce tu contraseña elegida:\n")
seguridad=True

for i in range(len(password)):
	if (len(password)<8 or password[i]==" "):
		seguridad=False

if seguridad==True:
	print("La contraseña es segura")
else:
	print("La contraseña no es segura. Intente nuevamente")


