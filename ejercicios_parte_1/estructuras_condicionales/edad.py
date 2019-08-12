from time import localtime

t = localtime()
t.tm_mday
t.tm_mon
t.tm_year
#   Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
def edad():
    dia = int(input('Ingrese su fecha de nacimiento. \nDía: '))
    mes = int(input('Mes: '))
    anio = int(input('Año: '))
    
    d = (t.tm_mday) - dia
    m = t.tm_mon - mes
    a = t.tm_year - anio

    if m < 0:
        print(f'Usted tiene {a - 1} años.')
    elif m == 0:
        if d < 0:
            print(f'Usted tiene {a - 1} años.')
        else:
            print(f'Usted tiene {a} años.')
    else:
        print(f'Usted tiene {a} años.')



edad()