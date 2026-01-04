#Ejercicio 1
#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir 
# dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
#Lista <<< [20, 50, "Curso", “Python”, 3.14]

#3 modificar elemntos

import os    # limpiar terminal 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()


lista = [20, 50, "Curso", "python" , 3.14]   # defino la variable lista

print(lista) # imprimo lista para que el ususario pueda ver las opciones
print('')

lista[0] = input('ingresa un valor cualquiera para sustituir el primer lugar: ') # esta variable me da elvalor de el primer lugar
lista[1] = input('ingrese un valor cualquiera para sustituir el segundo lugar: ') # esta variable me da el valor de el segundo lugar
print('') #espacio

print('la lista modificada es la siguiente: ', lista) #en esta salida se imprime la lista con los valores cambiados posicion 1 y 2


