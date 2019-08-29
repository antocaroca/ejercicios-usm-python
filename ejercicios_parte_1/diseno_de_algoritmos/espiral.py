#   Escriba un programa que entregue la suma de las diagonales en una
#  espiral de 1001 × 1001 creada de la misma manera.
# 1001 x 1001 = 1002001 = ultimo numero de la espiral -1000 = 1001001 ultimo numero diagonal sup izq -1000 = 1000001 ultimo numero diagonal inferior izq - 1000 = 999001 ultimo numero diagonal inferior derecha

diagonal_superior_derecha = []
dsd = 0
for i in range(1, 1002, 2):
    if i % 2 == 0 or i == 1:
        continue
    else:
        diagonal_superior_derecha.append(i**2)
        dsd += (i**2)
           
# print(dsd) 
# diagonal inferior izquierda 
cont = 0
suma  =0
for j in diagonal_superior_derecha:
    cont+=1
    suma += (j - (4*cont))
# print(suma)
# print("suma de los números de una diagonal sin el 1", dsd + suma)

c = 0
n = 499
uno = 1
siete = 7
diferencia = siete-uno # 6
total = 0
while c != 499:
    
    diferencia+=8 # 14 22
    siete += diferencia # 21
    total+=siete
    c+=1
# print(total+7)

c2 = 0
n2 = 499

uno2 = 1
tres = 3
diferencia2 = uno2-tres # -2
total2 = 0
while c2 != 499:
    diferencia2-=8 # -10
    tres += abs(diferencia2) # 
    total2+=tres
    c2+=1
    # print(tres)
# print(total2+3)
# print(total+7)
# print("suma de los números de una diagonal sin el 1", dsd + suma)
print("suma de las 2 diagonales:", (total2+3)+ (total+7)+(dsd + suma)+1)
   