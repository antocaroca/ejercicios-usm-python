#   Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, 
# pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos,
#  el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego,
#  en cuyo caso el resultado final es 7-6.

#   Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

def tenis():
    a = int(input('Ingrese juegos ganados por A: '))
    b = int(input('Ingrese juegos ganados por B: '))

    if a == 6 and b <= 4 or a == 7 and b == 5 or a == 7 and b == 6:
        print('Ganó A')
    elif b == 6 and a <= 4 or b == 7 and a == 5 or b == 7 and a == 6:
        print('Ganó B')
    else:
        print('juego inválido.')

tenis()