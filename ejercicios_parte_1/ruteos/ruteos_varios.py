#   Solácese ruteando los siguientes programas.
# j = 2
# c = 1
# p = True
# while j > 0:
#     j = j - c # 2 - 1
#     if p:
#         c = c + 1 # 2
#     p = not p # False
# print(j < 0 and p) # True

# a = 10
# c = 1
# x = 0
# y = x + 1 # 1
# z = y # 1

# while z <= y:
#     z = z + c # 2
#     y = 2 * x + z # 1
#     if y < 4:
#         y = y + 1 # 2
#     x = x - 1

# print(x, y, z) # -2 2 3

# a = 11
# b = a / 3 #  3.6
# c = a / 2 # 5.5
# n = 0

# while a == b + c: # no muestra nada
#     n += 1
#     b += c
#     c = b - c
#     if n % 2 == 0:
#         a = 2 * a - 3
#     print(100 * b + c)

a = True
b = '1'
c = 2
       # 1
while b[-1] not in '378':
    a = 0 == len(b) % 2 # 1
    if a:
        c = c * 7 # 2 * 7 = 14
    b = b + str(c) # 1 + 14 = 15
print(c)