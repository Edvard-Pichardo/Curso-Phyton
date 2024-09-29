#Condicionales
#< menor que
#> mayor que
#== igual que
#>= mayor igual
#<= menor igual
#!= diferente que

print("Programa de evaluación de notas de alumnos")

nota_alumno=input("Introduzca la nota del alumno: ")

def evaluaciones(nota):
	valoracion="aprobado"
	if nota<6:
		valoracion="suspenso"
	return valoracion	

print(evaluaciones(int(nota_alumno)))	