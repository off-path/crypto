from random import randint
from source import Point, gen_shared_secret
import hashlib
from Crypto.Cipher import AES

# Define the curve
p = 310717010502520989590157367261876774703
a = 2
b = 3

#sagemath
F = FiniteField(p)
E = EllipticCurve(F,[a,b])

# Generator
g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = E.point((g_x, g_y))

b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = Point(b_x, b_y)


P = E.point((280810182131414898730378982766101210916, 291506490768054478159835604632710368904))
iv = '07e2628b590095a5e332d397b8a59aa7'
encrypted_flag = '8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af'


print('factor E.order():', factor(E.order()))
#2^2 * 3^7 * 139 * 165229 * 31850531 * 270778799 * 179317983307

factors, exps = zip(*factor(E.order()))
primes = [factors[i]^exps[i] for i in range(len(factors))]
#[4, 2187, 139, 165229, 31850531, 270778799, 179317983307]

dlogs = []
for fac in primes:
  t = int(G.order() / fac)
  dlog = discrete_log(t*P, t*G, operation="+")
  dlogs += [dlog]
  print("factor: "+str(fac)+", Discrete Log: "+str(dlog))

print(dlogs)
[47836431801801373761601790722388100620, 1871, 73, 2080, 704661, 105138385, 109957133994]

#chinese remainder theoreme
n = crt(dlogs, primes)
if(P == n * G):
  print("n: ",n)
else:
  raise "error"

s = gen_shared_secret(B, n)
print(s)

sha1 = hashlib.sha1()
sha1.update(str(s).encode('ascii'))
key = sha1.digest()[:16]

iv = bytes.fromhex(iv)
encrypted = bytes.fromhex(encrypted_flag)

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(encrypted)
print(plaintext)