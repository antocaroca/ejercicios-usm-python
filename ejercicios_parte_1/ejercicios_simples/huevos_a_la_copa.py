#   Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida
#  el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

from math import pi, log


def huevo_a_la_copa(to):

    temp_original = 1
    M = 47  # Masa huevo chico
    M = 67  # Masa huevo grande
    c = 3.7  # Capacidad calorifica especifica
    p = 1.038  # Densidad
    K = 5.4 * 10 ** -3  # Conductividad termica
    tw = 100  # Temperatura de ebullicion del agua
    ty = 70  # Temperatura máx para el centro de la yema

    p1 = M ** (2.0/3) * c * p ** (1/3)
    p2 = K * pi**2 * (4 * pi / 3)**(2/3)
    p3 = log(0.76 * (temp_original - tw)/(ty - tw))

    return p1 / p2 * p3


print(huevo_a_la_copa(1))