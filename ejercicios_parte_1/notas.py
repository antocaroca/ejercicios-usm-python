"""
Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula.

NC=(C1+C2+C3)/3 ==> promedio de certámenes
C3 = ?
NF=NC⋅0.7+NL⋅0.3 ==> NL: promedio de laboratorio  NF: la nota final.

Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y 
muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
"""

def que_nota_necesito():
    nota_60 = 60
    c1 = int(input('Ingrese la nota del certamen 1: '))
    c2 = int(input('Ingrese la nota del certamen 2: '))
    nl = int(input('Ingrese la nota del laboratorio: '))

    nc = (nota_60 - (nl * 0.3)) / 0.7 # promedio notas 
    c3 = (nc * 3) - (c1 + c2)

    # nc = (c1 + c2 + c3) / 3
    # nc = (45 + 55 + 73) / 3 = 57.66

    # nf = (nc * 0.7) + (nl * 0.3)
    # nf = (57.66 * 0.7) + (65 * 0.3) = 59.86
    return print(f"Necesita nota {c3: .2f} en el certamen 3")

que_nota_necesito()

# Ingrese nota certamen 1: 45
# Ingrese nota certamen 2: 55
# Ingrese nota laboratorio: 65
# Necesita nota 72 en el certamen 3

# nl * 0.3 = 19.5
# (promedio_notas * 0.7) + (19.5) = 60
# (promedio_notas * 0.7)  = 60 - 19.5
# (promedio_notas * 0.7)  = 40.5 / 0.7
# promedio_notas = 57.857....


# 45 + 55 + c3 / 3 = 57.857
# 45 + 55 + c3 = 57.857 * 3
# 100 + c3 = 17380989798
# c3 = 1738098 -100
# c3 = 73









