#   Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma 
# de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe 
# entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese un número: '))
n3 = 0

# print(f"La suma es {sum(range(n1 + 1, n2))}.")    # primera solución

for i in range(n1+1, n2):   # segunda solución
    n3 += i
print(f"La suma es {n3}.")
   
    
    

