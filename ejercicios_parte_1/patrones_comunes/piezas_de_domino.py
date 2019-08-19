#   Desarrolle un programa que permita determinar la cantidad total de puntos que contiene un juego de dominó de 28 piezas.

suma = 0
count = 0

for i in range(0,7):
    suma+=i
    count+=1    
seis = ((count*6) + suma)

suma2 = 0
count2 = 0

for i in range(0,6):
    suma2+=i
    count2+=1   
cinco = ((count2*5) + suma2)

suma3 = 0
count3 = 0

for i in range(0,5):
    suma3+=i
    count3+=1   
cuatro = ((count3*4) + suma3)

suma4 = 0
count4 = 0

for i in range(0,4):
    suma4+=i
    count4+=1   
tres = ((count4*3) + suma4)

suma5 = 0
count5 = 0

for i in range(0,3):
    suma5+=i
    count5+=1   
dos = ((count5*2) + suma5)

suma6 = 0
count6 = 0

for i in range(0,2):
    suma6+=i
    count6+=1   
uno = ((count6*1) + suma6)

print("El total de puntos es:", uno+dos+tres+cuatro+cinco+seis)
