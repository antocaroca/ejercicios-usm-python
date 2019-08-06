#   Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
def  centimetros_a_pulgadas():
    longitud = float(input('Ingrese longitud: '))
    pulgadas = longitud / 2.54
    return f"{longitud} cm equivalen a {pulgadas : .4f} pulgadas."

print(centimetros_a_pulgadas())