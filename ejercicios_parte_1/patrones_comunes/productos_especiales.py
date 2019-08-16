#   Escriba sendos programas que pidan al usuario la entrada correspondiente y calculen las siguientes operaciones:
#   1 ) El factorial n! de un número entero n≥0, definido como:
#   n!=1⋅2⋅3⋅⋯⋅n.
#   Además, se define 0!=1.

n = int(input('Ingrese n: '))
fact = 1

for i in range(n, 0, -1): # lista inversa de números
    fact*=i  # contador que multiplica la lista 
print("factorial de n:", fact) 


#   2 ) La potencia factorial creciente n**m, definida como:
#   n**m = n(n+1)(n+2)⋯(n+m−1).

m = int(input('Ingrese m: '))
fact_crec = 1

for i in range(m):
    fact_crec *= n * (n+m)
print("factorial creciente:", fact_crec)

#   3) El coeficiente binomial (nk), definido como:
#   (nk) = n⋅(n−1)⋅(n−2)⋅⋯⋅(n−k+1) / 1⋅2⋅3⋅⋯⋅k = n! / (n−k)!k!

k = int(input('Ingrese k: '))

fact_k = 1
for i in range(k, 0, -1): 
    fact_k*=i   
print("factorial de k:", fact_k) 

fact_n_k = 1

for i in range((n - k), 0, -1): 
    fact_n_k*=i   
print("factorial de n menos k:", fact_n_k)

coef = fact / (fact_k * fact_n_k)

print("coeficiente binominal:", (int(coef)))











