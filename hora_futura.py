#   Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h,
#  que indique qué hora marcará el reloj dentro de h horas:
def fun_hora_futura():
    hora_actual = int(input('Ingrese la hora actual: '))
    cantidad_horas = int(input('Ingrese un número entero de horas para saber qué hora marcará el reloj dentro de esas horas: '))
    if hora_actual + cantidad_horas <= 12:
        return print(f"Hora actual: {hora_actual} \nCantidad de horas: {cantidad_horas} \nEn {cantidad_horas} horas, el reloj marcará las {hora_actual + cantidad_horas}.")    
    else:
        return print(f"Hora actual: {hora_actual} \nCantidad de horas: {cantidad_horas} \nEn {cantidad_horas} horas, el reloj marcará las {(cantidad_horas % 12) - (12 - hora_actual)}.")    

        
fun_hora_futura()