#Ejercicio 2: Clasificador de Estaciones
#Objetivo: Determinar la estación del año según el mes ingresado.
#Descripción:
#•	El programa pedirá al usuario que ingrese un número de mes (1-12).
#•	Clasificará el mes en su estación correspondiente: 
#o	Invierno: Diciembre, Enero, Febrero
#o	Primavera: Marzo, Abril, Mayo
#o	Verano: Junio, Julio, Agosto
#o	Otoño: Septiembre, Octubre, Noviembre
#•	Si se ingresa un número fuera de rango, mostrará un mensaje de error
import os 
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

#defino variables
# pido ingresar el valor de la variable en nuemro entero
mes = int(input('''Digite un numero segun el mes para determinar la estacion del año
1 enero, 2 febrero, 3 marzo, 4 abril, 5 mayo, 6 junio, 7 julio, 8 agosto,
9 septiembre, 10 octubre, 11 noviembre, 12 diciembre:  '''))

print(' ') # genero el espacio para que el texto se vea mas limpio

match mes :   # dependiendo el # digitado te imprime la condicion
    case 1 :  
        print('la estacion del año es= invierno')    #segun la entrada en #entero se imprime una salida segun la condiciona que se cumpla
    case 2 :
        print('la estacion del año es= invierno')
    case 3 :
        print('la estacion del año es= primavera')
    case 4 :
        print('la estacion del año es= primavera')
    case 5 :
        print('la estacion del año es= primavera')
    case 6 :
        print('la estacion del año es= verano')
    case 7 :
        print('la estacion del año es= verano')
    case 8 :
        print('la estacion del año es= verano')
    case 9 :
        print('la estacion del año es= otoño')
    case 10 :
        print('la estacion del año es= otoño')
    case 11 :
        print('la estacion del año es= otoño')
    case 12 :
        print('la estacion del año es= invierno')
    case _ :
        print('digitaste un valor diferente al pedido') #si digitas una letra o otroa caracter diferente al pedido te saldra este mensajeç
        