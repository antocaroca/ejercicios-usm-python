""" Escriba un programa que pida al usuario ingresar la inversión inicial y el porcentaje de tasa de descuento.
 A continuación, debe preguntar el flujo de dinero estimado para cada mes y mostrar 
cuál es la parte entera del VAN hasta ese momento.
El programa debe terminar apenas el VAN comience a dar positivo.
"""
inversion_inicial = int(input('Ingrese Inversión Inicial: '))
tasa_descuento = int(input('Ingrese % tasa de descuento: '))


contador = 0
van = - (inversion_inicial)
while True:
    contador += 1
    flujo_por_mes = int(input(f'Flujo mes {contador}: '))
    van += (flujo_por_mes/(1+(tasa_descuento*0.01))**contador)
    if van > 0:
        break
    print('VAN:', int(van))
print('VAN:', int(van))
