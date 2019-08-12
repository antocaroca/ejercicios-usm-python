#   Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: 
# cada uno de los lados no puede ser más largo que la suma de los otros dos.

# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

# si acaso el triángulo es inválido; y
# si no lo es, qué tipo de triángulo es:
#   Triángulo equilátero: tiene todos sus lados iguales. 
#   Triángulo isósceles: tiene dos lados iguales. 
#   Triángulo escaleno: los tres lados son desiguales.
def triangulo():
    a = float(input('Ingrese a: '))  
    b = float(input('Ingrese b: '))
    c = float(input('Ingrese c: '))
    # a + b
    # a + c
    # b + c 
    
    if a == b and a == c:
        print('es triángulo equilátero.')
    elif a != b and a != c and b != c and a <= (b + c) and b <= (a + c) and c <= (a + b):
        print('es triángulo escaleno')
    elif a == b or a == c or b == c and a <= (b + c) and b <= (a + c) and c <= (a + b):
        print('es triángulo isósceles.')
    else:
        print('no es un triángulo válido.')

triangulo()