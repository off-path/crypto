def euclide_etendu(a, b):
    # Assurez-vous que a est le plus grand des deux nombres
    if a < b:
        a, b = b, a

    print(f"Initialisation - a: {a}, b: {b}")

    # Initialisation des variables pour l'algorithme d'Euclide étendu
    a, b = a, b
    coefficient_s1 = 1
    coefficient_s2 = 0
    coefficient_t1 = 0
    coefficient_t2 = 1

    # Algorithme d'Euclide étendu
    iteration = 1
    while b > 0:
        # Calcul du quotient et du reste de la division de a par b
        print(f"Divmod de a: {a}, b: {b}")
        quotient, reste = divmod(a, b)
        print(f"Iteration {iteration} - Quotient: {quotient}, Reste: {reste}")

        # Mise à jour des variables
        print(f"Mise à jour {iteration} - Avant: a: {a}, b: {b}, Coef_s1: {coefficient_s1}, Coef_s2: {coefficient_s2}, Coef_t1: {coefficient_t1}, Coef_t2: {coefficient_t2}")
        a, b = b, reste
        print(f"Mise à jour {iteration} - Apres: a: {a}, b: {b}")

        # Mise à jour des coefficients de Bézout
        print(f"Mise à jour {iteration} - Avant: Coef_s1: {coefficient_s1}, Coef_s2: {coefficient_s2}")
        coefficient_s1, coefficient_s2 = coefficient_s2, coefficient_s1 - quotient * coefficient_s2
        print(f"Mise à jour {iteration} - Avant: Coef_s1: {coefficient_s1}, Coef_s2: {coefficient_s2}")
        
        print(f"Mise à jour {iteration} - Apres: Coef_t1: {coefficient_t1}, Coef_t2: {coefficient_t2}")
        coefficient_t1, coefficient_t2 = coefficient_t2, coefficient_t1 - quotient * coefficient_t2
        print(f"Mise à jour {iteration} - Apres: Coef_t1: {coefficient_t1}, Coef_t2: {coefficient_t2}")

        iteration += 1

    # Retourne le PGCD et les coefficients de Bézout
    print(f"Fin de l'algorithme - PGCD: {a}, Coef_s: {coefficient_s1}, Coef_t: {coefficient_t1}")
    return a, coefficient_s1, coefficient_t1


def inverse_euclide_etendu(resultat_euclide):
    # Inverse les résultats du PGCD et des coefficients de Bézout
    reste, coefficient_s, coefficient_t = resultat_euclide
    print(f"Inversion des résultats - Avant: PGCD: {reste}, Coef_s: {coefficient_s}, Coef_t: {coefficient_t}")
    return reste, coefficient_t, coefficient_s


# Exemple d'utilisation
a = 3
b = 17

# Applique l'algorithme d'Euclide étendu
resultat_euclide = euclide_etendu(a, b)

# Affiche les résultats
print(f"Algorithme d'Euclide étendu - PGCD: {resultat_euclide[0]}, Coef_u: {resultat_euclide[2]}, Coef_v: {resultat_euclide[1]}")

# Inverse les résultats du PGCD et des coefficients de Bézout
resultat_inverse_euclide = inverse_euclide_etendu(resultat_euclide)
print(f"Inversion des résultats - PGCD: {resultat_inverse_euclide[0]}, Coef_u: {resultat_inverse_euclide[1]}, Coef_v: {resultat_inverse_euclide[2]}")
