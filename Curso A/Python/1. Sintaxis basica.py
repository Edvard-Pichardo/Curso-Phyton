print ("Hola Mundo")
#Esto es un comentario

mi_nombre="Mi nombre es Cristian"
print (mi_nombre)

tu_nombre= "Tu nombre es\
 Pedro"
print (tu_nombre)

a=0
for i in range(5):
   a+=1
   print (a)

#suma
5+6 
#resto de una division
10%3
#exponente
5**3
#Division entera
9//2
#Division
9/2

#Declarar una variable
#nombre
#Nombre
#nombre3
#mi_nombre
#my_name_is

#Tipos de variable
numero=5
name= "Cristian"
numbre= 5.2
print (type(numero)) #type nos permite ver el tipo de nuestro contenedor
print (type(name))
print (type(numbre))

mensaje="""Esto es un mensaje
con tres saltos
de linea"""
print (mensaje)

#Condicional if
numero1=5
numero2=7
if numero1>numero2:
  print ("El numero 1 es mayor")
else: 
  print ("El numero 2 es mayor")

#Funciones

#Declaracion
def mensaje3():
        #Cuerpo de la funcion
	print ("Estamos aprendiendo Python")
	print ("Hola Mundo, otra vez xd")
	print ("Estamos aprendiendo mucho")
#Llamada
mensaje3()
mensaje3()
mensaje3()

def suma():
	num1=5
	num2=7
	print (num1+num2)

suma()
def suma(num1, num2):
	
	print (num1+num2)

suma(2,2)
suma(5,3)
suma(3,12)

def restainversa(num1, num2):
	resultado=num1+num2
	return resultado

print(restainversa(1,2))

#Listas
miLista=["Maria", "Pepe","Antonio", "Marta", 5, True, 523.3, "Antonio"]
print(miLista[:])
print(miLista[2])
print(miLista[0])
print(miLista[-1])

#Porciòn delista
print(miLista[0:3])
print(miLista[:3])
print(miLista[:2])
print(miLista[1:2])
print(miLista[1:3])

print(miLista[2:])
print(miLista[1:])

miLista.append("Sandra")
print(miLista[:])

miLista.insert(2,"MariLuz")
print(miLista[:])

miLista.extend(["Juan", "Felipe", "Ana", "Lucia"])
print(miLista[:])

print(miLista.index("Maria"))
print(miLista.index("Felipe"))
print(miLista.index("Antonio"))

print("pepe" in miLista)
print("Pepe" in miLista)

print(miLista[5])
print(miLista[6])

miLista.remove(523.3)
miLista.remove("MariLuz")
print(miLista[:])


miLista.pop()
print(miLista[:])

miLista2=[3, 4, 12, 990, "Ana Maria"]

miLista3=miLista+miLista2
print(miLista3[:])

miLista4=[3, 4, 12, 990]*3
print(miLista4[:])

#Tuplas
mitupla=("Juan",13, 0, 13, 13, 1, 1995)
print(mitupla[2])
print(mitupla[0])

miLista5=list(mitupla)
print(miLista5[:])
print(mitupla[:])

mitupla2=tuple(miLista5)
print(mitupla2[:])
print(miLista5[:])

print("Juan" in mitupla)
print("Pedro" in mitupla)

print(mitupla.count(13))
print(mitupla.count("Juan"))

print(len(mitupla))

#Tupla unitaria
mitupla3=("Pedro",)
print(len(mitupla3))

#Empaquetado de tupla
mitupla4="Juan", "Pedro", "Felipe"
print(mitupla4[:])

#Desempaquetado de tupla
mitupla5=("Juan", 13, 1, 1995)
a, b, c, d=mitupla5
print(mitupla5[:])
print(a)
print(b)
print(d)
print(c)

#No se puede modificar las tuplas como las listas.

#Diccionarios
#Asocian datos clave:valor
#Paises y capitales

midic={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido": "Londres", "España":"Madrid"}
print(midic["Francia"])
print(midic["España"])
print(midic)

midic["Italia"]="Lisboa"
print(midic)

midic["Italia"]="Roma"
print(midic)

del midic["Reino Unido"]
print(midic)

midic2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midic2)

mitupla9=["España", "Francia", "Reino Unido", "Alemania"]
midic3={mitupla9[0]:"Madrid", mitupla9[1]:"Paris", mitupla9[2]:"Londres", mitupla[3]:"Berlin"}
print(midic3)

midic4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]}
print(midic4)
print(midic4["Anillos"])

midic5={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midic5)
print(midic5["Anillos"])

print(midic5.keys())
print(midic5.values())
print(len(midic5))


#En python todo esun objeto

