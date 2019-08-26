fila_alfil = int(input('Fila alfil: '))
columna_alfil = int(input('Columna torre: '))

fila_torre = int(input('Fila torre: '))
columna_torre = int(input('Columna torre: '))


# torre gana
# if columna_torre == columna_alfil or fila_torre == fila_alfil:
#   print('Torre captura')

#gana alfil
if abs(fila_alfil - fila_torre) == abs(columna_alfil - columna_torre):
  print('torre gana')



