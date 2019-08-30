#   Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen respectivamente $270, $340 y $390.
#  La máquina acepta y da de vuelto monedas de $10, $50 y $100.
producto_A = 270
producto_B = 340
producto_C = 390
monedas = 0

eleccion = input('Elija producto: ')

if eleccion == 'A':
    money = int(input('Ingrese monedas: '))
    while monedas != producto_A:
        monedas+=money
        if monedas == producto_A:
            break
        elif monedas > producto_A:
            print(f'Su vuelto: {monedas-producto_A}')
            break
      # AQUI QUEDÉ...

