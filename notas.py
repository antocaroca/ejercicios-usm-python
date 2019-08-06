"""
Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula.

NC=(C1+C2+C3)/3 ==> promedio de certámenes
C3 = ?
NF=NC⋅0.7+NL⋅0.3 ==> NL: promedio de laboratorio  NF: la nota final.

Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y 
muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
"""
nota_60 = 0
def que_nota_necesito():
    c1 = int(input('Ingrese la nota del certamen 1: '))
    c2 = int(input('Ingrese la nota del certamen 2: '))
    nl = int(input('Ingrese la nota del laboratorio: '))
    nc = (c1 + c2 + c3) / 3
    nf = (nc * 0.7) + (nl * 0.3)
    return print(f"Necesita nota {c3} en el certamen 3")


# Ingrese nota certamen 1: 45
# Ingrese nota certamen 2: 55
# Ingrese nota laboratorio: 65
# Necesita nota 72 en el certamen 3
