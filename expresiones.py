# Evaluación de expresiones
# Sin usar el computador, evalúe las siguientes expresiones, y para cada una de ellas indique el resultado y su tipo (si la expresión es válida) o qué error ocurre (si no lo es):

# >>> 2 + 3      # Respuesta: tipo int, valor 5
# >>> 4 / 0      # Respuesta: error de división por cero
# >>> 5 + 3 * 2     # Respuesta: 11
# >>> '5' + '3' * 2     # Respuesta:'335' (error) ==> 533 (correcto)
# >>> 2 ** 10 == 1000 or 2 ** 7 == 100  # Respuesta: False
# >>> int("cuarenta")  # Respuesta: error type  ==> ValueError: invalid literal for int() with base 10: 'cuarenta' (correcto)
# >>> 70/16 + 100/24    # Respuesta: 8.541 ==> 8.541666666666668 (correcto)
# >>> 200 + 19%     # Respuesta:238 (error) ==> SyntaxError: invalid syntax (correcto)
# >>> 3 < (1024 % 10) < 6 # Respuesta: True
# >>> 'six' + 'eight'   # Respuesta: 'sixeight'
# >>> 'six' * 'eight'    # Respuesta: error ==> TypeError: can't multiply sequence by non-int of type 'str'
# >>> float(-int('5') + int('10')) # Respuesta: error ==> 5.0 (correcto)
# >>> abs(len('ocho') - len('cinco')) # Respuesta: error ==> 1 (correcto)
# >>> bool(14) or bool(-20)     # Respuesta: error ==> True (correcto)
# >>> float(str(int('5' * 4) / 3)[2])   # Respuesta: error ==> 5.0 (correcto) ????  x khe!?
# Compruebe sus respuestas en el computador.