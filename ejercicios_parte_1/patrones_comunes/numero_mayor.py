#    Escriba un programa que permita determinar el número mayor perteneciente a un conjunto de n números,
#  donde tanto el valor de n como el de los números deben ser ingresados por el usuario.

n = int(input('Ingrese un n: '))
i = 0
mayor = 0

while i < n:
    i += 1
    c = int(input('Ingrese un número: '))
    if c > mayor:
        mayor = c
    
  
print("El mayor es:", mayor)

    
  

