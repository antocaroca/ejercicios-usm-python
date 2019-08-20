#   Escriba un programa que determine la cantidad de dígitos en un número entero ingresado por el usuario:

n = int(input('Ingrese un dígito: '))
num = n

contador = 0

r = 0

while n > 0:
    u = n % 10
    n = int(n/10)
    r = r * 10 + u 
    contador+=1
   

if contador <= 1:
    print(f"{num} tiene {contador} dígito.")
    if num == 0:
        print(f"0 tiene 1 dígito.")
else: 
    print(f"{num} tiene {contador} dígitos.")