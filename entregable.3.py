

import os
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()


def analizar_estudiantes (estudiantes1, estudiantes2): # defino la funcion
    
    return { 
        "estudiantes_ambos_grupos" : estudiantes1 & estudiantes2,
        "estudiantes_solo_1ergrupo" : estudiantes1 - estudiantes2,
        "estudiantes_solo_2dogrupo" : estudiantes2 - estudiantes1,
        "estudiantes_unidos" : estudiantes1.union(estudiantes2)
    } # retorno de una vez las formulas que debo aplicar

estudiantes1 = {"maria", "isabel", "sebastian", "armando"} # realizo los grupos
estudiantes2 = {"maria", "isabel", "guillermo", "esteban"}

resultado = analizar_estudiantes(estudiantes1,estudiantes2) # declaro el resultado y llamo la funcion para poderla imprimir

print(resultado) # imprimo resulatado
print()

print(" mostrando el resultado organizado =")
print()

for categoria, estudiantes in resultado.items():
    print(f"{categoria}:{estudiantes}") # itero en las categorias y cada uno de los estudiantes y en el resultado para mostrar el mensaje organizado
