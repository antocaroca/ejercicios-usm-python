#   Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.
#   Para calcular el dígito verificador, se deben realizar los siguiente pasos:
#   Obtener el rol sin guión ni dígito verificador.
#   Invertir el número. (e.g: de 201012341 a 143210102).
#   Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, 
# si es que se acaban los números, se debe comenzar denuevo, por ejemplo, con 143210102:
#   1× 2 +4× 3 +3× 4 +2× 5 +1× 6 +0× 7 +1× 2 +0× 3 +2× 4 =52
#   Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11 ---- 52 % 11 = 8
#   Con el resultado obtenido en el paso anterior, debemos restarlo de 11:  11 − 8 = 3
#   Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.


rol = 201012341
rol2= rol
r = 0
secuencia = 1
suma = 0

while rol > 0:
    u = rol % 10
    rol = int(rol/10)
    r = r * 10 + u
    
    secuencia+=1
    if secuencia > 7:
        secuencia = 2
    # print("u", u, "secuencia", secuencia, "=", u*secuencia)
    suma = suma + (u*secuencia)
    
resultado = 11- (suma%11)

# print(r)
#print("secuencia", secuencia)
# print("suma", suma)
# print(resultado)
print(f"dígito verificador: {rol2}-{resultado}")


