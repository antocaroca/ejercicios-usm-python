"""
Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre
 dos sumandos consecutivos sea menor que 0,0001. Recuerde que el factorial n! es el producto de los números de 1 a n.
"""
# fórmula factorial de n
n = 1
fact = 1

while True:

    for i in range(n, 0, -1): # lista inversa de números
        fact*=i  # contador que multiplica la lista 
    # print("factorial de n ingresado:", fact) 
    # print("1/factorial:", 1/fact) 

# fórmula si ya sé el factorial de n:
# siguiente factorial ==> n × (n-1)!
    siguiente_fact = (n + 1) * fact

    # print("siguiente factorial", siguiente_fact)
    # print("1/siguiente_fact:", 1/siguiente_fact)

    resta =  (1/fact) - (1/siguiente_fact)
    # print("resta:", resta)


    if resta < 0.0001:
        print("resta:", resta)
        break
    else:
        n +=1
        



