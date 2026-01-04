import os    # borro terminal
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

# creacion de agenda telefonica
print('Agenda telefonica')
print('')
print(''' contactos disponibles en la agenda de contactos
      sebastian lopez
      gustavo petro
      daniel quintero''')
print('')
diccionario_Contactos = {'sebastian lopez' : '3137921336', 'gustavo petro' : '3106666666', 'daniel quintero' : '3139999999'}
nombre = input('escribe el nombre del contacto: ')
nombre = nombre.lower()

if nombre in diccionario_Contactos :
    print(f'el numero de telefono de {nombre} es = {diccionario_Contactos[nombre]}')
else :
    print('nombre de contacto no encontrado')
