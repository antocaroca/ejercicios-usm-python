#   Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida
#  el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

def huevo_a_la_copa():
    temp_original = float(int('Ingrese la temperatura original del huevo: '))

    M = 47 g #    Masa huevo chico
    M = 67 g#    Masa huevo grande
    c = 3.7 [J g -1 K -1] #   Capacidad calorifica especifica
    p = 1.038 [g cm -3] #    Densidad
    K = 5.4 * 10 -3 [W cm -1 K -1] #    Conductividad termica
    tw = 100 °C #  Temperatura de ebullicion del agua
    ty = 70 °C #   Temperatura máx para el centro de la yema

