#   Escriba un programa que muestre una tabla de multiplicar como la siguiente:
#   Los números deben estar alineados a la derecha.

for i in range(1,11): 
    for j in range(1,11): 
        if j*i < 10:
            print(' ', j*i, end=' ')
        elif (j*i)>=100:
            print(j*i, end='')
        else:
            print('', j*i, end=' ')
    print('') 
