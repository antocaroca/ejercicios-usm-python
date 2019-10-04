n_dias = int(input('Cuántos días? '))
i = 0
lista_precios = []
lista_dias = []

while i < n_dias:
    i += 1
    dia = float(input(f'Dia {i}: '))
    lista_precios.append(dia)
    lista_dias.append(i)

indice_par = []
indice_impar = []
# par = (list(zip(lista_dias, lista_precios)))
for index in enumerate(lista_precios):
    if index[0] % 2 == 0:
        indice_par.append(index[1])
    else:
        indice_impar.append(index[1])

par = (list(zip(indice_par, indice_impar)))


