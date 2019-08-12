#   Escriba un programa que simule una calculadora básica, este puede realizar operación de suma,
#  resta, multiplicación y división.
def calculadora():
    n1 = int(input('ingrese el primer número: '))
    n2 = int(input('ingrese el segundo número: '))
    operador = input('Ingrese: +, -, *, /  :')
    
    if operador == '+':
        return print(n1 + n2)
    elif operador == '-':
        return print(n1 - n2)
    elif operador == '*':
        return print(n1 * n2)
    elif operador == '/':
        if n2 == 0:
            return print('no se puede dividor por cero.')
        else:
            return print(n1 / n2)

calculadora()     
