#Operadores lógicos and y or
#AND= y si adémas
#OR= o si no
#IN= en

print("Programa de becas año 2021")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce número total de hermanos: "))
print(numero_hermanos)

salario_familia=int(input("Introduce salario familiar al mes: "))
print(salario_familia)

if distancia_escuela>40 and numero_hermanos>2 or salario_familia<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")