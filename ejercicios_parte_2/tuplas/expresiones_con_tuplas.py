a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

#   Sin usar el computador, indique cuál es el resultado y el tipo de las siguientes expresiones. 
# A continuación, verifique sus respuestas en el computador.
print(
a < b, '\n',    # True
y + w, '\n'     # 9?
x + a, '\n',    # 27, 3 2, 10, 1991
len(v), '\n',   # 2
v[1][1], '\n',  # 10
c[0][0], '\n',  # 'Donald'
z, y, '\n',     # ((27, 3), 9)
a + b[1:5], '\n',   # 
(a + b)[1:5], '\n', #
str(a[2]) + str(b[2]), '\n',    #
str(a[2] + b[2]), '\n',     #
str((a + b)[2]), '\n',      #
str(a + b)[2]       #
)