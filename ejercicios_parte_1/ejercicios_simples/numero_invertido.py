#   Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
def inverso():
    n = int(input('Ingrese un entero de 3 digitos: '))
    # print("El número invertido es: " + str(digitos[2]) + str(digitos[1]) + str(digitos[0]))

    r = 0
    while n > 0:
        ultimo = n % 10   # 789%10 = 9  //// 78%10 = 8  //// 7%10 = 7
        n = int(n / 10)   # 789/10 = 78     //// 7  //// 7/10 = 0
        r = r * 10 + ultimo # 0*10+9= 9     //// 9*10+8 = 98    //// 98*10 +7 = 987 <-----resultado
        # print (ultimo, n, r) <--- ruteo de variables

    print (r)


inverso()
