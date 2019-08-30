cont = 0
cert = 0
while cont < 3:
    cont += 1
    c = float(input(f'C{cont}: '))
    cert+=c
    if c < 2 and cont == 2:
        print('Reprobado')
        break
    elif c > 9 and cont == 2:
        print('Aprobado')
        break
    elif (cert/cont) < 3 and cont == 3:
        print('Reprobado')
    elif (cert/cont) <= 7 and cont == 3:
        exam = float(input('Examen: '))
        if exam < 5:
            print('Reprobado')
        else:
            print('Aprobado')
    elif (cert/cont) > 3 and (cert/cont) < 7 and cont == 3:
        exam = float(input('Examen: '))
        if exam < 5:
            print('Reprobado')
        else:
            print('Aprobado')

    
    