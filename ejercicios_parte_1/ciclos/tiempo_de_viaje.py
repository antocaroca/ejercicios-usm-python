#   Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
#  entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

total = 0
while True:
    tiempo = int(input('Duración tramo: '))
    
    total+=tiempo
    
    if tiempo == 0:
        break

minutos = int(total%60)
if minutos < 10:
    minutos = "0" +str(minutos)


print(f"tiempo total viaje {int(total/60)}:{minutos}")
  



    