#   Escriba un programa que reciba como entrada una palabra e indique si es palíndromo o no.

p = input('Ingrese una palabra: ')

if p == p[::-1]:
    print("es palíndromo.")
else:
    print("no es palíndromo.")

#   Modifique su programa para que reconozca oraciones palíndromas. La dificultad radica en
#  que hay que ignorar los espacios:

o = input('Ingrese oración: ')
o = o.replace(' ', '')

if o == o[::-1]:
    print('Es palíndromo')
else:
    print('no es palíndromo')