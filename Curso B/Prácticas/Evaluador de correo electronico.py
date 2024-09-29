#Evaluador de correo electronico

#Evalua en función de si tiene una única "@" o uno o mas "."

mail=input("Introduce tu correo eléctronico:\n")
arroba=0
punto=0

for i in range(len(mail)):
	if mail[i]=="@":
		arroba=arroba+1
	if mail[i]==".":
		punto=punto+1
if (0<arroba<2 and punto>=1):
	print("El correo es correcto")
else: 
	print("El correo es incorrecto")