import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

# entrada nombre de la persona
nombre = input(' Por favor ingrese su nombre : ')
apellidos = input('Por favor ingrese sus apellidos: ')

# entrada ingresos mensuales
ingresos = float(input('Por favor ingrese el valor de sus ingresos mensuales: '))
subsidio = 0
# menu nievel educativo alcanzado
print(''' por favor ingresa el numero correspondiente a su nivel educativo alcanzado
      1 - Basico 
      2 - Media 
      3 - Universitario ''')

nivel_Educativo = int(input('Digita el numero correspondiente al nievel educativo alcanzado: '))

# estructurar las condicionales
match nivel_Educativo:
    case 1 if ingresos < 1000000:
        subsidio = 30
    case 1 if ingresos >= 1000000 and ingresos <= 2000000:
        subsidio = 20
    case 1 if ingresos > 2000000:
        subsidio = 10
    case 2 if ingresos > 1200000:
        subsidio = 28
    case 2 if ingresos >= 1200000 and ingresos <= 2200000:
        subsidio = 18
    case 2 if ingresos > 2200000:
        subsidio = 8
    case 3 if ingresos < 1500000:
        subsidio = 25
    case 3 if ingresos >= 1500000 and ingresos <= 2500000:
        subsidio = 15
    case 3 if ingresos > 2500000:
        subsidio = 5
    case _:
        print('los datos ingresados son incorrectos')
        
print(f'''Resultado de subsidio
          Nombre = {nombre}, {apellidos}
          Ingreso Mensual = {ingresos}
          Nivel_Educativo = {nivel_Educativo}
          Porcentaje nivel asignado = {subsidio}%
          Valor del subsidio = $ {ingresos*subsidio / 100}''')
