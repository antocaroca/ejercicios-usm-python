#   Una función cuadrados(l), que entregue una lista con los cuadrados de los valores de l:
def cuadrados(l):
    lista_cuadrados = []
    for element in l:
        lista_cuadrados.append(element**2)
    return print(lista_cuadrados)


cuadrados([1, 2, 3, 4, 5])
cuadrados([3.4, 1.2])