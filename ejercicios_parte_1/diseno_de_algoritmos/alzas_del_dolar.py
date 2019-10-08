n_dias = int(input('Cuántos días? '))
i = 0
dicc_precios = {}
dia_impar = []
dia_par = []

while i < n_dias:
    i += 1
    dia = float(input(f'Dia {i}: '))
    dicc_precios[i]=dia

for dia, precio in dicc_precios.items():
    if dia % 2 != 0:
        dia_impar.append(precio)
    else:
        dia_par.append(precio)

pares = (list(zip(dia_impar, dia_par)))
resultado = []
for p in pares:
    resultado.append(abs(p[0]- p[1]))


print("{0:.2f}".format(max(resultado), 2))
