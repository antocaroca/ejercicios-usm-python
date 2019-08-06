import math
#   Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, 
# y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

def triangulo_rectangulo():
    cat_a = int(input('Ingrese la longitud del cateto a: '))
    cat_b = int(input('Ingrese la longitud del cateto b: '))
    hipotenusa = math.sqrt((cat_a**2) + (cat_b**2))
    print(f"La hipotenusa es {hipotenusa:.4f}")  
    

triangulo_rectangulo()