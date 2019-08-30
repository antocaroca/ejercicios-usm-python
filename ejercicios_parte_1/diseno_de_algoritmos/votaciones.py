# FALTA PROMEDIOS
nu = int(input('Número de universidades: '))
i = 0
a = 0
r = 0
n = 0
b = 0

while i < nu: # esto se va a repetir 3 veces
    i+=1 # contador hasta 3
    nombre = input('Universidad: ') # ingreso nombre universidad
    while True: # se repetirá este ciclo infinitamente

        voto = input('Voto: ') # ingreso voto
        if voto == 'A': # si es a 
            a+=1 # 'a' es igual a  'a' más 1
        elif voto == 'R':
            r +=1
        elif voto == 'N':
            n += 1
        elif voto == 'B':
            b+=1
        elif voto == 'X':
            break # término del ciclo
    # print(f'{nombre}: {a} aceptan, {r} rechazan, {b} blancos, {n} nulos')
    

print(f'Universidades que aceptan: {a}')
print(f'Universidades que rechazan: {r}')
