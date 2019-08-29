#   Entre todos los enteros mayores a 1 hay solamente cuatro que pueden ser representados por la suma de los cubos de sus dígitos.
# FALTA!
start= 149
end = 410
count = 0
lista = []

while start < end:
    start += 1
    count+=1
    lista.append(start)
print(lista)

cubos = []

for cubo in range(1,10):
    cubos.append(cubo**3)

print(cubos)
