#   Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, 
# y le entregue su condición de riesgo.
def imc():
    height = float(input('Ingrese su estatura en metros: '))
    weight = float(input('Ingrese su peso en kilos: '))
    age = int(input('Ingrese su edad: '))

    imc = weight / (height ** 2)
    if age < 45:
        if imc < 22.0:
            print('imc bajo')
        elif imc >= 22.0:
            print('medio')
    elif age >= 45:
        if imc < 22.0:
            print('imc medio')
        elif imc >= 22.0:
            print('alto')



imc()