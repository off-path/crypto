from Crypto.Util.number import getPrime, inverse, long_to_bytes
import random
import math
import numpy as np

FLAG = b'crypto{?????????????????????}'


def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.randint(2, upper_bound)
    while True:
        g = random.randint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
    h = (inverse(f, q)*g) % q
    return (q, h), (f, g)


def encrypt(q, h, m):
    assert m < int(math.sqrt(q // 2))
    r = random.randint(2, int(math.sqrt(q // 2)))
    e = (r*h + m) % q
    return e


def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

# q et h forment la clef public
q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800

# e est le flag chiffé
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

###     On peut construire un trellis formé par les deux vecteurs
###     de la matrice suivante:     M (1,h),(0,q)


def dot_product(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))

def norm_squared(v):
    return dot_product(v, v)

def subtract_vectors(v1, v2, scalar):
    return [x - scalar * y for x, y in zip(v1, v2)]

def reduce_vectors(v1, v2):
    while True:
        if norm_squared(v2) < norm_squared(v1):
            v1, v2 = v2, v1
        
        m = round(dot_product(v1, v2) / dot_product(v1, v1))
        
        if m == 0:
            return v1, v2
        
        v2 = subtract_vectors(v2, v1, m)

# Assuming your h and q are defined as before
v = [1, h]
u = [0, q]

v1, v2 = reduce_vectors(u, v)
f, g = v1[0], v1[1]
# Decrypt function as before
# Use the decrypt function here with the new f and g values

print("crypto{",long_to_bytes(decrypt(q,h,f,g,e)),"}")