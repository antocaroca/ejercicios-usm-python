""" Escriba un programa que pregunte a cada jugador cuál es su jugada, 
muestre cuál es el marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres rondas.
 Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra."""
#   tijera le gana a papel, 
# papel le gana a piedra, 
# piedra le gana a tijera,
#  y todas las demás combinaciones son empates.
ronda = 0
contador_a = 0
contador_b = 0

while ronda < 6:
    a = input('A: indique su jugada: ')
    b = input('B: indique su jugada: ')
    ronda+=1
    if a == 'tijera' and b == 'papel':
        contador_a += 1
        print(f"{contador_a}  -  {contador_b}")
    elif b == 'tijera' and a == 'papel':
        contador_b += 1
        print(f"{contador_a}  -  {contador_b}")
    elif a == 'papel' and b =='piedra':
        contador_a += 1
        print(f"{contador_a}  -  {contador_b}")
    elif b == 'papel' and a =='piedra':
        contador_b += 1
        print(f"{contador_a}  -  {contador_b}")
    elif a == 'piedra' and b == 'tijera':
        contador_a += 1
        print(f"{contador_a}  -  {contador_b}")
    elif b == 'piedra' and a == 'tijera':
        contador_b += 1
        print(f"{contador_a}  -  {contador_b}")
    else:
        print(f"{contador_a}  -  {contador_b}")


 
print() 
if contador_a > contador_b:
    print('A es el ganador')
elif contador_b > contador_a:
    print('B es el ganador')
else:
    print('empate')
