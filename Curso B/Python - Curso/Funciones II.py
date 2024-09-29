# Funciones II: Parametros o argumentos

def suma():
	num1=3
	num2=4
	print(num1+num2)

suma()

def suma_mod(num3, num4):
	print(num3+num4)

suma_mod(1,4)
suma_mod(8,5)
suma_mod(5,1)
suma_mod(1.3,7)


def suma_return(a,b):
	resultado=a+b
	return resultado

print(suma_return(1,1))

almacena_resultados=suma_return(2,2)
print(almacena_resultados)
