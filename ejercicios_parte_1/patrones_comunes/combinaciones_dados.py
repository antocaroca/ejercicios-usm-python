#   Contar combinaciones de dados


k = int(input('Ingrese el puntaje: '))

fact_12 = 1

for i in range(12, 0, -1): # lista inversa de números
    fact_12*=i  # contador que multiplica la lista 
print("factorial de n:", fact_12) 

fact_k = 1
for i in range(k, 0, -1): 
    fact_k*=i   
print("factorial de k:", fact_k) 

fact_n_k = 1

for i in range((12 - k), 0, -1): 
    fact_n_k*=i   
print("factorial de n menos k:", fact_n_k)

combinaciones = fact_12 / (fact_n_k)

# print("combinaciones:", (int(combinaciones)))

# FALTA :(