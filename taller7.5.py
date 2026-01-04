#Ejercicio 5
#En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y
# muestre la capital de ese pais, en dado caso el pais no esté en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se 
# encuentra. Nota: si digito en minúsculas no debe haber problema ver método capitalize().

#{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras", "Nicaragua": "Managua", "Costa Rica": "San Jose",
# "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

import os    # borro terminal
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()
# defino lavariable de los paises
diccionario_paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
                      "Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires",
                      "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = (input('escribe un pais para ver su capital: ')) # el ususario ingresa
pais = pais.capitalize() # combierto la primera letra en mayuscula

if pais in diccionario_paises:  # condicionales si se cumple imprime primer mensaje
    print(f'la capital de {pais} es : {diccionario_paises}' )
else : # sino imprime pais no encontrado
    print('pais no encontrado')