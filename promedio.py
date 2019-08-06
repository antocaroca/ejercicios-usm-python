#   Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
def promedio():
    nota1 = float(input('Ingrese la primera nota: '))
    nota2 = float(input('Ingrese la segunda nota: '))
    nota3 = float(input('Ingrese la tercera nota: '))
    nota4 = float(input('Ingrese la cuarta nota: '))
    total = nota1 + nota2 + nota3 + nota4
    return f"El promedio de las 4 notas es {total/4}."

print(promedio())