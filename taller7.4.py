#Ejercicio 4
#Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, 
# es la letra que debe imprimir el programa.

import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()



alfabeto = ( 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print('este es el alfabeto','' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
numero = int(input('por favor ingresa un numero: '))
numero1 = numero-1
print('')
print(f'la letra correspiondiente al alfabeto del numero digitado es: ', alfabeto[numero1])
