#   ¿Existen otros valores p que sean el n-ésimo primo, tales que espejo(p) es el espejo(n)-ésimo primo? 21
n = 73
espejo = 37
n_esimo_primo = 0
for num in range(1, n + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           num
           n_esimo_primo+=1

print('n-esimo primo:', n_esimo_primo)
