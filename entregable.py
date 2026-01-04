import os
def limpiar_terminal():
    os.system('cls')
    
limpiar_terminal()
globals().clear()

# entregable 1 nivel basico
conjunto_1 = {1,2,3,4,5} # conjunto numero 1 con los numero del 1 al 5
print(conjunto_1)
#agregar el numero 6

conjunto_1.add(6) # add para agregar un solo elemento el numero 6 al conjunto_!
print(conjunto_1) # para ver como queda el conjunto agregando el numero 6

conjunto_1.remove(3) # quito el numero 3 con remove ya que se cual es el nmero que tengo que eliminar
print(conjunto_1) #para ver el conjunto_1 sin el numero 3



