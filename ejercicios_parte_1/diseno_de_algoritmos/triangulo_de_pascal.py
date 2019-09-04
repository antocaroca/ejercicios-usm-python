#   Genere las primeras 20 líneas. Considere que en la línea 20 aparecen números de cinco dígitos.
c = 0
d = 0
e = 0
f = 0
for i in range(1, 21):
    print('1', i, c +i, d+c+i, e+d+c+i, f+e+d+c+i)
    c+= i
    d+=c
    e+=d
    f+=e