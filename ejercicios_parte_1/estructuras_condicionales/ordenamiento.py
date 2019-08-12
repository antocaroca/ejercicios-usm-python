#   Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
def n2_ordenados():
    n1 = int(input('Ingrese el primer número: '))
    n2 = int(input('Ingrese el segundo número: '))
    
    if n1 < n2:
        print(n1, n2)
    else:
        print(n2, n1)
                
n2_ordenados()

#   A continuación, escriba otro programa que haga lo mismo con tres números:
def n3_ordenados():
        n1 = int(input('Ingrese el primer número: '))
        n2 = int(input('Ingrese el segundo número: '))
        n3 = int(input('Ingrese el tercer número: '))
        
        min_value = (min((n1, n2, n3)))
        max_value = (max((n1, n2, n3)))
        mid_value = (n1 + n2 + n3) - (min_value + max_value)
        print(min_value, mid_value,max_value)
                             
n3_ordenados()

#       Finalmente, escriba un tercer programa que ordene cuatro números:

def n4_ordenados():
        n1, n2, n3, n4 = map(int, input('ingrese 4 números separados por un espacio: ').strip().split()) # se ingresan los números uno al lado del otro, separados por un espacio.
        r = sorted((n1, n2, n3, n4))
        print(r[0], r[1], r[2], r[3])

n4_ordenados()