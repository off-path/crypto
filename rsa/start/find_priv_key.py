def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
ciphertext = 77578995801157823671636298847186723593814843845525223303932

N = p * q
phi_N = (p - 1) * (q - 1)

d = mod_inv(e, phi_N)

print("Private key (d):", d)

m = pow(ciphertext, d , N)

print("Decrypted message (m):", m)
