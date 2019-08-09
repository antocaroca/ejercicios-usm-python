# 1. Escriba la función es_divisible(n, d) que indique si n es divisible por d:
def es_divisible(n, d):
    if n % d == 0:
        print('n es divisible por d')
    else:
        print('n no es divisible por d')

# es_divisible(4, 2)
# es_divisible(5, 2) 

#   Usando la función es_divisible, escriba una función es_primo(n) que determine si un número es primo o no:

def es_primo(n):
    for d in range(2, n):
        if n % d == 0:
            return print('no es primo')
    return print('es primo') 
    
    
es_primo(21)



