from scalar_multiplication import scalar_mul 
import hashlib

#Y2 = X3 + 497 X + 1768, p: 9739, G: (1804,5368) 
a = 497
b = 1768
p = 9739

def calculate_shared_secret(QA,nB):
    S = scalar_mul(QA,nB)
    
    # hashage de x
    x_str = str(S[0])
    sha1 = hashlib.sha1()
    sha1.update(x_str.encode())
    shared_secret = sha1.hexdigest()
    
    return shared_secret


G = (1804,5368) 
QA = (815, 3190)
nB = 1829

print(calculate_shared_secret(QA,nB))

