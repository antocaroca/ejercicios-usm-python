"""
Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que
 la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
Recuerde que el factorial n! es el producto de los números de 1 a n.
"""
# fórmula si ya sé el factorial de n:
# siguiente factorial ==> n! = n × (n-1)!

# fórmula factorial de n
n = int(input('Ingrese n: '))
fact = 1
for i in range(n, 0, -1): # lista inversa de números
    fact*=i  # contador que multiplica la lista 
print("factorial de n ingresado", fact)  # 1 dividido en resultado

siguiente_fact = (n + 1) * fact

print("siguiente factorial", siguiente_fact)

suma = (1/fact) + (1/siguiente_fact)

print("suma: ", suma)

resta = (1/fact) - (1/siguiente_fact)

if resta < 0.0001:
    print("resta:", resta)
else:
    print('es mayor')



