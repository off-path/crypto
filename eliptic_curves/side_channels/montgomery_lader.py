from sympy import sqrt_mod

p = 2**255 - 19
A = 486662
B = 1
g_x = 9
g_y = sqrt_mod(9**3+486662*9**2+9,p)
k = 0x1337c0decafe

#find the x-coordinate (decimal representation) of point Q = [0x1337c0decafe] G 

def inv_mod(x,p):

    if x == 0:
        return 0
    
    return pow(x, p-2, p)

def add_points(x1, y1, x2, y2):

    if x1 == x2 and y1 == y2:
        return double_point(x1, y1)
    
    alpha = ((y2 - y1) * inv_mod(x2 - x1, p)) % p
    x3 = (B*alpha**2 - A - x1 - x2) % p
    y3 = (alpha * (x1 - x3) - y1) % p

    return x3, y3

def double_point(x1, y1):

    alpha = ((3*x1**2 + 2*A*x1 + 1) * inv_mod(2*B*y1, p)) % p
    x3 = (B*alpha**2 - A - 2*x1) % p
    y3 = ((alpha * (x1 - x3) - y1)) % p

    return x3, y3


def montgomery_ladder(k, Gx, Gy):
    #Initialiser RO et R1
    R0x, R0y = Gx, Gy
    R1x, R1y = double_point(Gx, Gy)

    # k en binaire
    k_bin = bin(k)[2:]

    # Itération suivant la représentation binaire de k, en partant du bit de poids faible
    for bit in k_bin[1:]: # on commence à l'indice 1 pour sauter le bit de poids le plus élevé qui est toujours 1
        if bit == '0':
            R1x, R1y = add_points(R0x, R0y, R1x, R1y)
            R0x, R0y = double_point(R0x, R0y)

        else:
            R0x, R0y = add_points(R0x, R0y, R1x, R1y)
            R1x, R1y = double_point(R1x, R1y)

    return R0x



res = montgomery_ladder(k, g_x, g_y)
print(res) 