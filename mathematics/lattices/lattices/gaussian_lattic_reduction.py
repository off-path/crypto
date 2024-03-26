import numpy as np

# Les vecteurs v et u sont définis comme des listes, convertissez-les en arrays NumPy pour les opérations.
v = np.array([846835985, 9834798552])
u = np.array([87502093, 123094980])

def reduce_vectors(v1, v2):
    while True:
        # (a) Swap si ||v2|| < ||v1||
        if np.linalg.norm(v2) < np.linalg.norm(v1):
            v1, v2 = v2, v1
        
        # (b) Calcul de m
        m = round(np.dot(v1, v2) / np.dot(v1, v1))
        
        # (c) Si m = 0, retourner v1, v2
        if m == 0:
            return v1, v2
        
        # (d) Mise à jour de v2
        v2 = v2 - m * v1

v1_reduced, v2_reduced = reduce_vectors(v, u)

# The flag is the inner product of the new basis vectors. 
flag = np.dot(v1_reduced, v2_reduced)

print(flag)