#Operador lógico in

print("Asignaturas optativas año 2021")
print("Asignaturas:")
print("Informátiva gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()

if asignatura in("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: "+ asignatura)
else:
	print("La asignatura escogida no está contemplada por ahora :)")

#Python escase sensitive, es decir, distingue entre mayusculas y minusculas
# lower() transforma todo a minusculas
# upper() transforma todo a mayusculas