p = 29
ints = [11, 6, 14]

def is_quadratic_residue(ints):
    for x in ints:
        for a in range(1, p):
            if (a * a) % p == x:
                return a

result = is_quadratic_residue(ints)
print(result)