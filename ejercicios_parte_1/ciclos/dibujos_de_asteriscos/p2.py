#   Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

altura = int(input('Ingrese altura: '))
a = 0
for i in range(1, altura + 1):
    print(i*'*')