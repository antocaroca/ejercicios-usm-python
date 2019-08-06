#   Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
import math

def circulo():
    radio = float(input('Ingrese el radio del círculo: '))
    perimetro = (2 * math.pi) * radio
    area = math.pi * (radio ** 2)
    return f"El perímetro del círculo es {perimetro: .2f} y su area es {area: .2f}."


print(circulo())