#   Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
def palabra_mas_larga():
    pal1 = input('Ingrese la primera palabra: ')
    pal2 = input('Ingrese la segunda palabra: ')

    if len(pal1) > len(pal2):
        print(f'La palabra {pal1} tiene {(len(pal1)) - (len(pal2))} letras más que {pal2}.')
    elif len(pal2) > len(pal1):
        print(f'La palabra {pal2} tiene {(len(pal2)) - (len(pal1))} letras más que {pal1}.')
    else:
        print('Las dos palabras tienen el mismo largo.')


palabra_mas_larga()