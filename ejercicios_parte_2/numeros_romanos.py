#   Escriba la función romano_a_arabigo que reciba un string con un número en notación romana, y entregue el entero equivalente:
def romano_a_arabigo(nr):
    
    if nr == 'I':
        nr = 1
    elif nr == 'V':
        nr = 5
    elif nr == 'X':
        nr = 10
    elif nr == 'L':
        nr = 50
    elif nr == 'C':
        nr = 100
    elif nr == 'D':
        nr = 500
    elif nr == 'M':
        nr = 1000
    return print(nr)
    








romano_a_arabigo('MCMXIV')
romano_a_arabigo('XIV')
romano_a_arabigo('X')
romano_a_arabigo('IV')
romano_a_arabigo('DLIV')
romano_a_arabigo('CCCIII')