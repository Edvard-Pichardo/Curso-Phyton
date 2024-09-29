#Operadores lógicos (and, or)

#and = y ademas
#or = o si no
#in=

print("Programa de evaluación de becas Pichardo 2024-1")

distancia_escuela=int(input("Introduce la distancia a la escuela en km:\n"))
num_her=int(input("Introduce el número de hermanos:\n"))
salario=int(input("Introduce el salario anual bruto:\n"))

print("La distancia a la escuela es:", distancia_escuela)
print("El número de hermanos es:", num_her)
print("El salario introducido es: $"+ str(salario))

if distancia_escuela>40 and num_her>2 or salario<=20000:
	print("Tienes derecho a beca :)")
else:
	print("No cumples con los requisitos pare tener beca. :(")

#Se pueden concatenar todos los operadores lógicos que se necesiten
#No existe un límite en ello