#Condicionales II (else y elif)

# if - Si
#else - y si no es verdad // por el contrario


#print("Verificación de acceso.")

#edad_usuario=int(input("Introduce tu edad: "))

#if edad_usuario<18:
#	print("No puedes pasar.")
#elif edad_usuario>100:
#	print("Edad incorrecta.")
#else:
#	print("Puedes pasar.")


#print("¡El programa ha finalizado!")


print("Programa para evaluar alumnos")

nota=int(input("Introduce la nota del alumno: "))

if nota<5:
	print("Insuficiente")

elif nota<6:
	print("Suficiente")

elif nota<7:
	print("Casi")

elif nota<9:
	print("Notable")

elif nota>10:
	print("Nota incorrecta")

else:
	print("Sobresaliente")








