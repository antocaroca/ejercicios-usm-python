# VOTACIONES DE LA CONFECH
nu = int(input('Número de universidades: '))
i = 0
k = 0

aceptan = 0
rechazan = 0
empate = 0

for uni in range(1, nu + 1):
    universidad = input('Universidad: ')
    a = 0
    r = 0
    b = 0
    n = 0

    while i < nu:

        voto = input('Voto: ')
        if voto == 'A':
            a+=1
        elif voto == 'R':
            r+=1
        elif voto == 'B':
            b+=1
        elif voto == 'N':
            n+=1
        elif voto == 'X':
            break
    print(f'{universidad}: aceptan {a}, rechazan {r}, blancos {b}, nulos {n}')
    if a > r:
        aceptan += 1
    elif r > a:
        rechazan += 1
    elif a  == r:
        empate += 1

print(f'Universidades que aceptan: {aceptan}')
print(f'Universidades que rechazan: {rechazan}')
print(f'Universidades que con empate: {empate}')
