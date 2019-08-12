#   Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos.
#  En caso que sea letra, determine si es mayúscula o minúscula.
def letra_o_numero():
    tecla = list(input('Ingrese algo: '))

    letra_nim = ['a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z']
    letra_may = ['A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z']
    num = ['1,2,3,4,5,6,7,8,9,0']

    for i in tecla:
        for j in num:
            if i in j:
                return print('es numero')
            for k in letra_nim:
                if i in k:
                    return print('es letra minuscula')
            for l in letra_may:
                if i in l:
                    return print('es letra mayucula')
                else:
                    return print('No es letra ni numero')
      
            
letra_o_numero()