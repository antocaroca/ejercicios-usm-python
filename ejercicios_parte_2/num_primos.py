# 1. Escriba la función es_divisible(n, d) que indique si n es divisible por d:
def es_divisible(n, d):
    if n % d == 0:
        print('n es divisible por d')
    else:
        print('n no es divisible por d')

es_divisible(4, 2)
es_divisible(5, 2) 

#   Usando la función es_divisible, escriba una función es_primo(n) que determine si un número es primo o no:

def es_primo(n):
    es_divisible(n, d=n)
    if n % 1 != 0 and n%n != 0:
        print("es primo")
    else:
        print('no es na primo')

    

es_primo(11)

# numero primo = es divisible por 1 y por sí mismo

# la funcion toma 2 parametros:
# 1) el número a comprobar si es divisible (dividendo)
# 2) el numero por el cual se divide (divisor)
