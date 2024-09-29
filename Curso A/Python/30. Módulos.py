#30.1 Módulos

#import Funciones

#Funciones.suma(7,5)
#Funciones.resta(9,5)
#Funciones.multiplica(2,6)

#from Funciones import * #suma

#suma(7,5)
#resta(10,5)
#multiplica(5,8)



#En aplicaciones complejas se puede solo importar una sola clase para optimizar código y así no se utiliza el código completo.



from Módulo_vehiculos import *

miCoche=vehiculos("Azul", "Rojo")

miCoche.estado()

