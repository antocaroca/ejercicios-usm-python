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
y + w, '\n',     # 9? x  ====>  12  ////  w = 3 , = 9 
x + a, '\n',    # (27, 3, 2, 10, 1991)
len(v), '\n',   # 2
v[1][1], '\n',  # 10
c[0][0], '\n',  # 'Donald' X ======> D  /// índice 0 de la primera palabra
z, y, '\n',     # ((27, 3), 9) X =====> 27 9   /// 
a + b[1:5], '\n',   # out of range :v  =======> (2, 10, 1991, 12, 1990)  //// Se incluye todo a, en b se hace un slice desde index 1 hasta el final (no importa que el corte exeda la longitud de la lista) y al final se suman las listas
(a + b)[1:5], '\n', # (2, 19, 1991, 25, 12) X =====> (10, 1991, 25, 12) //// se suma primero a +b y luego se aplica el slice
str(a[2]) + str(b[2]), '\n',    # 19911990 
str(a[2] + b[2]), '\n',     # type error X =====> 3981 //// se convierte todo el () a str y luego se suma
str((a + b)[2]), '\n',      # 1991
str(a + b)[2]     # 1991 x  ======> ,   ///// se suma a + b y todo se convierte a string incluso () , espacios en blanco
)