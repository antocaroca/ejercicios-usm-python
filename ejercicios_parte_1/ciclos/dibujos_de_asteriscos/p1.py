#   Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

altura = int(input('Ingrese altura: '))
ancho = int(input('Ingrese ancho: '))

for i in range(1, altura + 1):
    print(ancho * ('*'), end=' ')
    print()
    
print()
    

        