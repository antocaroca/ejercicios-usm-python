# Escriba un programa que:
# pregunte al usuario cuántos datos serán ingresados,
# pida al usuario ingresar los datos uno por uno, y
# entregue como resultado el rango de los datos.

n = float(input('cuántos valores ingresará? '))
i = 0
cont = 0
mayor = 0
lista = []
menor = 0
v = 0
while i < n:
    i+=1
    cont+=1
    valor = float(input(f'valor {cont}: '))
    lista.append(valor)
    if valor > mayor:
        mayor = valor
    
lista.sort()
# print(f'El rango es {mayor - lista[0]:.2f}')
print(menor)