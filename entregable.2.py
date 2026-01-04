
# nivel intermedio

frutas_1 = {"babanas", "papayas", "uvas", "mandarinas"} #conjunto de fruas1
frutas_2 = {"mandarinas", "moras", "mangos"} #conjunto de frutas2

frutas_3 = frutas_1 & frutas_2
print(frutas_3) # las frutas comunes son: utilizo & para que me de los elementos comunes
print(f"las frutas comunes son {frutas_3}")

frutas_4 = frutas_1 - frutas_2
print(frutas_4) # para mostrar las frutas qeu solo estan en el conjunto 1 utilizo primero frutas 1  - frutas 2 para que me muestre los que estan solo en frutas 1
print(f"las frutas que solo estan en el primer conjunto son {frutas_4}")

frutas_5 = frutas_1 ^ frutas_2 # utilizo el signo diferencia simetrica para que me arroje los eleementos que no se repiten
print(frutas_5) #para ver las frutas que no se repiten
print(f"las frutas que no se repiten entre los dos conjuntos son {frutas_5}")