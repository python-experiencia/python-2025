#Ejercicio 2
#Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean 
# multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos.

import os   #limpiar terminal
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()


print('de la siguiente lista voy a multiplicar la posicion 4,7 y 9 por 2 ') #mensaje para el ususario
print(1,2,3,4,5,6,7,8,9,10) # mensje del conjunto de numeros

lista = [1,2,3,4,5,6,7,8,9,10] #defino la variable

lista[3]*=2 # saco el valor  de la posicion4 y lo multiplico por 2
lista[6]*=2 # saco el valor  de la posicion7 y lo multiplico por 2
lista[8]*=2 # saco el valor  de la posicion9 y lo multiplico por 2

print('la lista modificada es:', lista) #mensjae d e salida con la variable modificada con los cambios


