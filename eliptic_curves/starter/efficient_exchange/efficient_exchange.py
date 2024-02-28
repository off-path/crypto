import sys
from pathlib import Path

parent_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_folder))

from scalar_multiplication import scalar_mul
from decrypt import decrypt_flag 


#Y2 = X3 + 497 X + 1768, p: 9739, G: (1804,5368)  
a = 497
b = 1768
p = 9739

def calculate_shared_secret(G,q_x,nB):
    #La seul différence avec curves_and_logs est que non avons Q(4726, ?)
    #On a 2 y disponible pour un x, on peut donc tester les deux x et voir lequel flag
    y = find_y_coordinates(q_x)

    QA0 = (q_x, y[0])
    QA1 = (q_x, y[1])

    print("QA0: ",QA0)
    print("QA1: ",QA1)

    if QA0[1] % 4 == 3:
        secret = scalar_mul(QA0, nB)
        flag = decrypt_flag(secret[0], iv, encrypted_flag)
        return flag
    
    else:
        secret = scalar_mul(QA1, nB)
        flag = decrypt_flag(secret[0], iv, encrypted_flag)
        return flag

    return

def find_y_coordinates(q_x):
    # Calcul du terme à droite de l'équation de la courbe elliptique
    right_side = (q_x**3 + 497*q_x + 1768) % p
    
    # Calcul des racines carrées modulo p
    sqrt_values = [y for y in range(p) if (y**2) % p == right_side]
    
    return sqrt_values

G = (1804,5368) 
q_x = 4726
nB = 6534

iv = "cd9da9f1c60925922377ea952afc212c"
encrypted_flag = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"


print(calculate_shared_secret(G,q_x,nB))

