#Números impares del 1 al 100
#Deberán aparecer el uno al lado del otro sin salto de línea

for i in range(100):
	if (i%2!=0):
		print(i, end=" ")

#Otra manera de hacerlo, más optimizado

print("\nOtra forma de hacerlo:")
for i in range(1,100,2):
	print(i, end=" ")