#    Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
def bisiesto():
    anio = int(input('Ingrese un año: '))
    if anio < 1582:
        if anio % 4 == 0:
            print(f'El año {anio} es bisiesto.')
        else:
            print(f'El año {anio} NO es bisiesto.')
    else:
        if anio % 400 == 0 or anio % 4 == 0 and anio % 100 != 0:
            print(f'El año {anio} es bisiesto.')              
        else:
            print(f'El año {anio} NO es bisiesto.')
            
        
bisiesto()

