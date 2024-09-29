#Ejercicio 4. Dirección email

usuario=input("Introduce tu nombre de usuario: ")

arroba=usuario.count('@')

if (arroba!=1 or (usuario.rfind('@')==len(usuario)-1) or usuario.find('@')==0):
	print("Tu usuario es incorrecto")
else:
	print("Tu usuario es correcto.")
