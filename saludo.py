#   Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamándolo por su nombre.

def saludo():
    nombre = input('Ingrese su nombre: ')
    return f"Hola {nombre}"

print(saludo())