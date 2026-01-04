#Ejercicio 1: Calculadora Básica
#Objetivo: Implementar una calculadora que realice operaciones básicas.
#Descripción:
#1.	El programa solicitará:
#a.	Primer número decimal
#b.	Segundo número decimal
#c.	Operación a realizar (+, -, *, /,**)
#2.	Debe calcular y mostrar el resultado de la operación seleccionada.
#3.	Si se ingresa una operación no válida, mostrará un mensaje de error.
#4.	Considerar el manejo de división por cero.

import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()


#defino la variable que va ingresar el ususario

operacion = (input('ingrese la operacion que  desea que realice la calculadora (*,-,/,**);  '))

match operacion : # match compara la condicion operacion (valor dado por el ususario operacion a realizar)
    case '*' :    # si da * realiza multiplicacion
        n1 = float(input('digite el primer numero1: '))
        n2 = float(input('digite el segundo numero2: ' ))
        multiplicacion = n1 *n2 # formula y defino variable multiplicacion
        print(f'el resultado de n1*n2 es=', multiplicacion) #imprimo el resultado
    case '-' :   # si ingresa - realiza resta
        n1 = float(input('digite el primer numero1: '))
        n2 = float(input('digite el segundo numero2: '))
        resta = n1 - n2# defino formula y la variable resta
        print(f'el resultado de n1- n2 es=', resta) # imprimo resultado
    case '/' : # si ungresa / realiza divicion
        n1 = float(input('digite el primer numero1: '))
        n2 = float(input('digite el segundo numero2: '))
        divicion = n1 / n2 # defino la formula y defino variable divicion
        print(f'el resultado de n1/n2 es=', divicion)
    case '**' : #si ingresa ** realzia potencia
        n1 = float(input('digite el primer numero1: '))
        n2 = float(input('digite el segundo numero2: ' ))
        potencia = n1 ** n2 # defino formula y variable potencia
        print(f'el resultado de n1**n2 es= ', potencia)
    case _ :
        print('no digitaste un valor valido') # si digita una valor diferente imprime esto
        
