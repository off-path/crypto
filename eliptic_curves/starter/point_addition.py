from Crypto.Util.number import inverse

# E: Y2 = X3 + 497 X + 1768, p: 9739 
a = 497
b = 1768
p = 9739



def point_add(P, Q):

    O = (0,0)
    if P == O:
        return Q
    if Q == 0:
        return P
    
    x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
    
    if x1 == x2 and y1 == -y2:
        return 0
    
    # if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
    if P != Q:
        lam = ((y2 - y1) * inverse(x2 - x1, p)) % p
    # If P = Q: λ = (3 * x1**2 + a) / 2 * y1
    else:
        lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) %p
    
    x3 = (lam**2 - x1 - x2)%p
    y3 = (lam * (x1 - x3) - y1)%p

    return (x3,y3)

# P=(493,5564)
# Q=(1539,4742)
# R=(4403,5202)
# print(point_add(point_add(point_add(P,P),Q),R))