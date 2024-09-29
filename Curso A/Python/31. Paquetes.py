#31. Paquetes

#Los paquetes son directorios donde se almacenarán módulos relacionados entre sí.
#Sirven para organizar y reutilizar el código
#Se crea unha carpeta con un archivo __init__.py

from Módulos.calculos_generales import *

dividir(10,2)

potencia(10,2)

redondear(25.84)

#Se pueden hacer subpaquetes, para ello se creará una carpeta dentro de la carpeta que ya estamos ocupando.
#Se crea el archivo __init__.py dentro de la subcarpeta
#Para incluirlo solamente se debe seguir la ruta.
		#from Módulos.calculos_generales.nombre_carpeta import *