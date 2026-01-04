#'''Problema 1 Sistema de Calificación de Notas

#Una institución educativa desea automatizar el proceso de asignación de menciones de honor a los estudiantes de acuerdo con su 
# nota final en una asignatura. La escala de calificación es la siguiente:
#· Si la nota es mayor o igual a 9.5 → "Mención de Excelencia"
#· Si la nota es mayor o igual a 8.0 y menor que 9.5 → "Mención de Honor"
#· Si la nota es mayor o igual a 6.0 y menor que 8.0 → "Aprobado"
#· Si la nota es menor que 6.0 → "Reprobado"
#Instrucciones:
#1. Solicita al usuario que ingrese su nombre.
#2. Solicita que ingrese la nota final (un número entre 0 y 10).

#3. Usa estructuras condicionales if/elif para determinar la mención según la nota.
#4. Muestra un mensaje personalizado como: "Estudiante [nombre], su mención es: [resultado]".
#5. Si el usuario ingresa una nota no válida, muestra un mensaje de error.

import os    # borro terminal
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

print('Segun las calificaciones obternidas su mension de honor es')
print('')
# entrada nombre del estudiante y defino la variable
nombre = input('por favor ingresa tu nombre completo: ')
print('')
# entrada nota final y defino la variable
nota = float(input('por favor ingresa la nota final: '))
print('')
# definir la estructura condicional
if nota >= 9.5 :
    nota_mension = 'Mension de Excelencia'
elif nota >= 8 and nota < 9.5 :
    nota_mension = 'Mension de Honor'
elif nota >= 6 and nota < 8 :
    nota_mension = 'Aprobado'
elif nota < 6 :
    nota_mension = 'Reprobado'
else :
    nota_mension = 'ingresaste un valor erroneo'

print(f' Estudiante {nombre}, su mension es {nota_mension}')
print('')
