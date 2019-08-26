#   Escriba un programa que muestre los números primos menores que m, donde m es ingresado por el usuario:
n = int(input('Primos menores que: '))

for num in range(1, n + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

