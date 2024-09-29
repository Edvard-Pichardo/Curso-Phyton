#Condicionales I (Condicion if)

#Flujo de instrucciones y ejecuciones 
#El orden es de arriba hacia abajo, por lo general.
#Las instrucciones de control de flujo modifican el orden de ejecucion
#Dada una condicion el condicional se ejecuta o no

#Sintaxis
# if condicion:
#      cuerpo de la condicion
# else:
#      cuerpo del else

print("Programa de evaluación de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")     #input hace que el fujo de ejecucion se detiene para agregar valores por teclado
                             
def evaluacion(nota):
	valoracion="Aprobado"
	if nota<5:
		valoracion="Suspendido"
	return valoracion

#print(evaluacion(4))
#print(evaluacion(8))

print(evaluacion(int(nota_alumno))) #int transforma elementos a enteros

