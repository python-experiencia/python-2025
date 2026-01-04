#Ejercicio 3
#Escribir una tupla con los meses del año, luego, pide al usuario un número, el que haya ingresado, es el mes que debe mostrar en la tupla.

import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()



tupla_meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
print(tupla_meses)
print('')

mes = int(input('digita un numero enterod el 1 al 12 para imprimir el mes correspondiente: '))
mes = mes-1
print(f'el mes correspondiente es; ', tupla_meses[mes])
