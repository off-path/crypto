from point_addition import point_add 
# E: Y2 = X3 + 497 X + 1768, p: 9739 
a = 497
b = 1768
p = 9739



def scalar_mul(P, n):
   
    O = (0,0)
    Q, R = P,O

    while n > 0:
        if n % 2 == 1:
            R = point_add(R, Q)
        Q = point_add(Q, Q)
        n //= 2
    return R
 
# X = (5323, 5438)
# n = 1337
# print(scalar_mul(X, n))

# P = (2339, 2213)
# n = 7863
# print(scalar_mul(P, n))