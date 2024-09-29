#29. Métodos de cadenas

#Uso de métodos de cadenas (objetos tipo string)
#La utilidad práctica es que a la hora de programar alguna aplicación es muy frecuente utilizar, manejar cadenas de caracteres.

#String: 

#upper(): convierte en mayusculas toda la letras de un string
#lower(): convierte en mayusculas toda la letras de un string
#capitalize(): Pone la primera letra en mayusculas.
#count(): Cuenta cuantas veces aparece una cadena de caracteres dentro de un texto.
#find(): Representa el indice/posición en el que aparece un grupo de caracteres dentro de un texto.
#isdigit(): Devuelve un True o False dependiendo si el valor es un dígito/ valor númerico o no lo es.
#isalum(): Comprueba si el caracter es alfanúmerico.
#isalpha(): Comprueba si hay solo letras (Los espacios no cuentan).
#split(): separa por palabras utilizando espacios.
#strip(): Borra los espacios sobrantes al inicio y al final.
#replace():cambiauna palabra o una letra por otra.
#rfind(): Hace lo mismo que find, representa el indice de un carácter pero contando desde atrás.


#Documentación de Python en google: Primer página es un compendio.
#Referencia de bibliotecas: http://pyspanishdoc.sourceforge.net/

#Dentro de "Referencia de bibliotecas" Entrar al punto 2.1.5 Tipos secuanciales y hasta abajo nos aparece "2.1.5.1 métodos de las cadenas"

#Ejemplos sencillos:

nombreUsuario=input("Introduzca tu nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())

print("El nombre es: ", nombreUsuario.lower())

print("El nombre es: ", nombreUsuario.capitalize())



edad=input("Introduce la edad que tienes: ")

while(edad.isdigit()==False):
	print("Por favor, introduce una edad real put0")
	edad=input("Introduce la edad que tienes: ")

if (int(edad)<18):
	print("No puedes pasar put0")
else:
	print("Puedes pasar, mi rey.")

