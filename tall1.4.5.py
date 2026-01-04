'''Ejercicio 5: Cálculo de áreas de figuras geométricas
Crea un programa en Python que muestre un menú interactivo en el que el usuario pueda seleccionar una figura geométrica 
(Esfera, Cubo, Cilindro, Pirámide). Una vez seleccionada la figura, el programa deberá solicitar los valores necesarios 
para calcular su volumen y mostrar el resultado.
Instrucciones:
1.	Muestra un menú con las siguientes opciones:
o	1. Esfera
o	2. Cubo.
o	3. Cilindro
o	4. Pirámide
2.	Pide al usuario que ingrese la opción correspondiente.
3.	Según la elección, solicita los valores requeridos:
o	Esfera: Radio.
o	Cubo: Lado
o	Cilindro: Radio y altura.
o	Pirámide: área de la base (lado a, lado b) y altura
4.	Calcula el área de la figura seleccionada.
5.	Muestra el resultado con un mensaje claro.
6.	Si el usuario ingresa una opción no válida, muestra un mensaje de error.
'''
import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()


# llamo de la libreria matematicas 
from math import pi
# defino variable
figura = int(input('''por favor ingresa el numero correspondiente a la figura que quieras calcularle el volumen
 1- esfera
 2- cubo
 3- cilndro
 4- piramide
 
=  '''))
print(' ')
# aplico los consicionales de match
match figura :
    case 1 :
        radio = float(input('digita el radio cms;'))
        vol_esfera = (4/3) * pi * radio**3 #esta formula me da el valor de vol_esfera
        print(f'el volumen de la esfera: {vol_esfera:.2f}', 'cms cubicos') # aplico :.2f con el fin que me muestre solo 2 decimales
    case 2 : 
        lado = float(input('ingresa la medida de uno de los lados del cubo en cms; '))
        vol_cubo = lado**3#esta formula me da el valor de vol_cubo
        print(f'el volumen del cubo: {vol_cubo:.2f}', 'cms cubicos')
    case 3 : 
        radio = float(input('ingresa la medida del radio en cms; '))
        altura =float(input('ingresa la medida de la altura del cilindro en cms; '))
        vol_cilindro = pi * radio**2 * altura #esta formula me da el valor de vol_cubo
        print(f'el volumen del cilindro: {vol_cilindro:.2f}', 'cms cubicos')
    case 4 :
        base = float(input('ingresa el valor del area de la  base de la piramide en cms: '))
        altura = float(input('ingresa la altura de la piramide en cms: '))
        vol_piramide = base * altura / 3 #esta formula me da el valor de vol_piramide
        print(f'el volumen de la piramide es: {vol_piramide:.2f}', 'cms cubicos')
    case _:
        print('numero de figuras incorrectos - revisa el numero corespondiente a la figura')
        #se imprime salida si no se cumple ninguna de las condiciones
        