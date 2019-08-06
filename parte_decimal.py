#   Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
def parte_decimal():
    num = float(input('Ingrese un número decimal: '))
    num = num - int(num)
    return print(f"La parte decimal del número ingresado es: {num: .2f}")

parte_decimal()