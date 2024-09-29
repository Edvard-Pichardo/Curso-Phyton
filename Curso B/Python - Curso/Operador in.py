#Operador in

#Case sensitive= Python distingue entre mayusculas y minusculas


print("Programa para la elección de asignaturas optativas de la carrera de Ingenieria 2024-1")
print("Asignaturas optativas:")
print("Informatica gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida:\n")
asignatura=opcion.lower()

if asignatura in ("informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura escogida: ", asignatura)
else:
	print("Ha surgido un error en el prgrama. La asignatura escogida no está contemplada en el programa.")

#Funcion.lower()  Escribe un valor a minusculas
#Función.upper()  Escribe un valor a mayusculas