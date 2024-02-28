p = 28151
res = []

# Parcourir chaque élément de Fp
for g in range(2, p):
    is_primitive = True

    # Générer toutes les puissances de g
    powers = set()
    for k in range(1, p):
        power = pow(g, k, p)
        if power in powers:
            # Si on trouve une puissance déjà rencontrée, g n'est pas primitif
            is_primitive = False
            break
        powers.add(power)

    if is_primitive:
        res.append(g)
        break 

print(res)
