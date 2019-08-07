#   Escriba la función invertir_digitos(n) que reciba un número entero n y entregue como resultado 
# el número n con los dígitos en el orden inverso:
def invertir_digitos():
    n_original = input('ingrese un número: ')
    n_inverso = (n_original[::-1])

    if n_original == n_inverso:
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")

    return print(n_inverso)


invertir_digitos()
