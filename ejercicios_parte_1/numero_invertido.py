#   Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
def inverso():
    digitos = list(input('Ingrese un entero de 3 dígitos: '))
    print("El número invertido es: " + str(digitos[2]) + str(digitos[1]) + str(digitos[0]))   

inverso()