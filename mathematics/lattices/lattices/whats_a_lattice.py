import numpy as np

v1 = np.array([6, 2, -3])
v2 = np.array([5, 1, 4])
v3 = np.array([2, 7, 1])

# produit vectoriel de v2 et v3
v2_cross_v3 = np.cross(v2, v3)

# produit scalaire de v1 et v2_cross_v3
volume = np.dot(v1, v2_cross_v3)

# valeur absolue pour obtenir le volume
volume_absolu = abs(volume)

print(volume_absolu)
