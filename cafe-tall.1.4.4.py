'''Ejercicio 4:  Menú de cafetería
Crea un menú interactivo donde el usuario pueda elegir entre café, té, jugo o agua. Usa match-case para mostrar 
el precio de la bebida seleccionada.
Ejemplo de entrada y salida:
'''
import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()


# definir ltexto incial
print('''En el siguiente menu encontraras las opciones de cafe que tenemos 
por favor digita le numero de la que quieres''')
print(' ') # genero un espacio para que el enunciado sea mas claro
print('1- cafe $3000')
print('2- te $2500')
print('3- juego $3500')
print('4- agua $2000')
print(' ')
#defino variable
bebida = int(input('ingrese el numero que identifica la bebida; '))

match bebida : #condicional match para variables bebida
    case 1 :
        print(f'haz seleccionado cafe, su precio es $3000') # si el # ingresado es 1 imprime este mensaje
    case 2 :
        print(f'haz seleccionado te, su precio es $2500')  #si el # ingresado es 2 imprime este mensaje
    case 3 :
        print(f'haz seleccionado jugo, su precio es $3500')  #si el # ingresado es 3 imprime este mensaje
    case 4 :
        print(f'haz seleccionado agua, su precio es $2000')  #si el # ingresado es 4 imprime este mensaje
    case _ :
        print('no haz digitado una opcion valida') # si ninguna de lasanteriores se cumple imprime este print.
