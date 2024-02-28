import math

v1 = (4, 1, 3, -1)
v2 = (2, 1, -3, 4)
v3 = (1, 0, -2, 7)
v4 = (6, 2, 9, -5)

# Fonction pour calculer le produit interne entre deux vecteurs
def inner_product(v, u):
    return sum(x * y for x, y in zip(v, u))

# Fonction pour calculer la taille d'un vecteur
def vector_size(v):
    return math.sqrt(sum(x**2 for x in v))

# Algorithme de Gram-Schmidt
def gram_schmidt(vectors):
    basis = [vectors[0]]  # Initialise la base avec le premier vecteur
    for i in range(1, len(vectors)):
        ui = list(vectors[i])  # Initialise ui avec vi
        for j in range(i):
            #vi * uj / size_of(uj)**2
            projection = inner_product(vectors[i], basis[j]) / vector_size(basis[j])**2
            #vi - projection * uj
            ui = [x - projection * y for x, y in zip(ui, basis[j])]
        basis.append(ui)
    return basis


# Calcul de la base orthogonale
orthogonal_basis = gram_schmidt([v1, v2, v3, v4])

print(orthogonal_basis)

# Affichage des composants du quatrième vecteur de la base orthogonale
print("Composants du quatrième vecteur de la base orthogonale:", orthogonal_basis[3])

# Affichage de la deuxième composante du quatrième vecteur de la base orthogonale
print("Deuxième composante du quatrième vecteur de la base orthogonale:", round(orthogonal_basis[3][1], 5))
