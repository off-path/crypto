g=3
#d= a trouver
p=13

# g*d =/ 1 % p
# 3*d =/ 1 % 13

if g**(p-1) % p == 1:
    #Fermat available
    # -> a**p-2 =/ 1 mod p
    # 3**11 =/ 1 mod 13
    d = g**(p-2) % p
    print(f"L'inverse multiplicatif de {g} modulo {p} est {d}")