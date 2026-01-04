
import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

'''Ejercicio 3: Calculadora de Impuestos Personalizada
Objetivo: Crear un sistema de cálculo de impuestos según rango de ingresos y estado civil.
Descripción:
•	El programa solicitará: 
1.	Monto de ingresos anuales
2.	Estado civil (Soltero, Casado, Divorciado)

•	Calculará impuestos según rangos y estado civil
•	A la salida, un mensaje donde indique el nombre y apellido de la persona, ingreso anual digitado, el porcentaje de impuesto que va a pagar y el valor del impuesto a pagar.
Rangos de Impuestos:
•	Soltero: 
o	Ingresos < $20,000: 10% de impuestos
o	Ingresos entre $20,000 y $50,000: 15% de impuestos
o	Ingresos > $50,000: 20% de impuestos
•	Casado: 
o	Ingresos < $30,000: 8% de impuestos
o	Ingresos entre $30,000 y $60,000: 12% de impuestos
o	Ingresos > $60,000: 18% de impuestos
•	Divorciado: 
o	Ingresos < $25,000: 9% de impuestos
o	Ingresos entre $25,000 y $55,000: 14% de impuestos
o	Ingresos > $55,000: 19% de impuestos
'''

#definir las variables
import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

# defino el texto inicial
print('1- soltero')
print('2- casado')
print('3- divorciado')

#defino las variables

estado = int(input(('ingresa el numero que representa tu estado civil:  '))) #ingresar dato tipo entero

nombre = input('ingresa tu nombre y apellidos: ') # ingresar un dato tipo texto

monto = float(input('ingresa el monto de ingresos anuales: ')) #ingresar un dato tipo entero


match  estado : # condiciono estado segun el estado
    case 1 if monto < 20000:   #genero una salida dependiendo del monto
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 10%')
        print(f'el valor del impuesto a pagar es =', monto * 0.1)
    case 1 if 20000 > monto < 50000 :  #genero una salida dependiendo del monto
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 15%')
        print(f'el valor del impuesto a pagar es =', monto * 0.15)
    case 1 if 50000 > monto : #genero una salida dependiendo del monto
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 20%')
        print(f'el valor del impuesto a pagar es =', monto * 0.2)
    case 2 if monto < 30000: #genero una salida dependiendo del monto
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 8%')
        print(f'el valor del impuesto a pagar es =', monto * 0.08)
    case 2 if 30000 > monto < 60000 : #genero una salida dependiendo del monto
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 12%')
        print(f'el valor del impuesto a pagar es =', monto * 0.12)
    case 2 if 60000 > monto :  #genero una salida dependiendo del monto
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 18%')
        print(f'el valor del impuesto a pagar es =', monto * 0.18)
    case 3 if monto < 25000:
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 9%')
        print(f'el valor del impuesto a pagar es =', monto * 0.09)
    case 3 if 25000 > monto < 55000 :
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 14%')
        print(f'el valor del impuesto a pagar es =', monto * 0.14)
    case 3 if 55000 > monto :
        print(f'hola ', nombre, 'su ingreso anual es de ', monto)
        print('el valor del impuesto es del 19%')
        print(f'el valor del impuesto a pagar es =', monto * 0.19)
    case _ :
        print('ingresaste un valor que no estaba en las opciones')
    # se genera esta salida si ninguna de las condicionaes se cumple
