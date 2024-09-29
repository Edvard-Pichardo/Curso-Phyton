#Programa para verificar correos electronicos

contador=0
contador2=0
contador3=0
mi_correo=input("Introduzca el correo a revisar: ")

for i in mi_correo:
	if i=="@":
		contador=contador+1
for j in mi_correo:
	if j==".":
		contador2=contador2+1
for k in mi_correo:
	if (k!="." and k!="@"):
		contador3=contador3+1

if (contador==1 and contador2>=1 and contador3>0):
	print("El correo es correcto")
else:
	print("El correo es incorrecto, vuelva a intentarlo")